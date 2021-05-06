import csv
from math import sqrt, exp, log
from scipy.stats import norm

global rows

def d(sigma, S, K, r, t):
    d1 = 1 / (sigma * sqrt(t)) * ( log(S/K) + (r + sigma**2/2) * t)
    d2 = d1 - sigma * sqrt(t)
    return d1, d2

def call_price(sigma, S, K, r, t, d1, d2):
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * exp(-r * t)
    return C

def put_price(sigma, S, K, r, t, d1, d2):
    P = -norm.cdf(-d1) * S + norm.cdf(-d2) * K * exp(-r * t)
    return P

#  Option parameters

def IV_call(pos):
	S = float(rows[pos][2])
	K = float(rows[pos][2])
	t = 90.0 / 365.0
	r = float(rows[pos][5]) / 100
	P0 = float(rows[pos][3])

	#  Tolerances
	tol = 1e-3
	epsilon = 1

	#  Variables to log and manage number of iterations
	count = 0
	max_iter = 1000

	#  We need to provide an initial guess for the root of our function
	vol = 0.20

	while epsilon > tol:
		#  Count how many iterations and make sure while loop doesn't run away
		count += 1.0
		if count >= max_iter:
			print('Breaking on count')
			break;

		#  Log the value previously calculated to computer percent change
		#  between iterations
		orig_vol = vol

		#  Calculate the value of the call price
		d1, d2 = d(vol, S, K, r, t)
		#  Here is where you put either call or put
		function_value = call_price(vol, S, K, r, t, d1, d2) - P0

		#  Calculate vega, the derivative of the price with respect to
		#  volatility
		vega = S * norm.pdf(d1) * sqrt(t)

		#  Update for value of the volatility
		vol = -function_value / vega + vol

		#  Check the percent change between current and last iteration
		epsilon = abs( (vol - orig_vol) / orig_vol )
		
	rows[pos][6] = vol

def IV_put(pos):
	S = float(rows[pos][2])
	K = float(rows[pos][2])
	t = 90.0 / 365.0
	r = float(rows[pos][5]) / 100
	P0 = float(rows[pos][3])

	#  Tolerances
	tol = 1e-3
	epsilon = 1

	#  Variables to log and manage number of iterations
	count = 0
	max_iter = 1000

	#  We need to provide an initial guess for the root of our function
	vol = 0.20

	while epsilon > tol:
		#  Count how many iterations and make sure while loop doesn't run away
		count += 1.0
		if count >= max_iter:
			print('Breaking on count')
			break;

		#  Log the value previously calculated to computer percent change
		#  between iterations
		orig_vol = vol

		#  Calculate the value of the call price
		d1, d2 = d(vol, S, K, r, t)
		#  Here is where you put either call or put
		function_value = put_price(vol, S, K, r, t, d1, d2) - P0

		#  Calculate vega, the derivative of the price with respect to
		#  volatility
		vega = S * norm.pdf(d1) * sqrt(t)

		#  Update for value of the volatility
		vol = -function_value / vega + vol

		#  Check the percent change between current and last iteration
		epsilon = abs( (vol - orig_vol) / orig_vol )
		
	rows[pos][6] = vol

def IV_writer():
	for pos in range(len(rows)):
		if rows[pos][1] == "P":
			continue
		else:
			IV_call(pos)

	for pos in range(len(rows)):
		if rows[pos][1] == "C":
			continue
		else:
			IV_call(pos)

# Calculate and write IV values for ADP
filename = "ADP.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

IV_writer()

file = open('ADP_IV.csv', 'w+', newline = '')
with file:
	write = csv.writer(file)
	write.writerows(rows)

# Calculate and write IV values for LMT
filename = "LMT.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

IV_writer()

file = open('LMT_IV.csv', 'w+', newline = '')
with file:
	write = csv.writer(file)
	write.writerows(rows)
	
	
# Calculate and write IV values for AIR
filename = "AIR.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

IV_writer()

file = open('AIR_IV.csv', 'w+', newline = '')
with file:
	write = csv.writer(file)
	write.writerows(rows)
