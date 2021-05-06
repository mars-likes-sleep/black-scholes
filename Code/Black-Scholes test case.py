from math import sqrt, exp, log
from scipy.stats import norm

# black-scholes formula: parity test case

def black_scholes_call(stock, strike, rfi, delta, time, sigma):
    d1_num = log(stock/strike) + (rfi - delta + 0.5 * sqrt(sigma)) * time
    d1_den = sigma * sqrt(time)
    d1 = d1_num / d1_den
    d1_prob = norm.cdf(d1)
    
    d2 = d1 - sigma * sqrt(time)
    d2_prob = norm.cdf(d2)
    
    bsc_1 = stock * exp(-delta * time) * d1_prob
    bsc_2 = strike * exp(-rfi * time) * d2_prob
    
    bsc = bsc_1 - bsc_2
    
    return bsc

def black_scholes_put(stock, strike, rfi, delta, time, sigma):
    d1_num = log(stock/strike) + (rfi - delta + 0.5 * sqrt(sigma)) * time
    d1_den = sigma * sqrt(time)
    d1 = d1_num / d1_den
    d1_prob = norm.cdf(d1)
    
    d2 = d1 - sigma * sqrt(time)
    d2_prob = norm.cdf(d2)
    
    bsp_1 = strike * exp(-rfi * time) * (1 - d2_prob)
    bsp_2 = stock * exp(-delta * time) * (1 - d1_prob)
    bsp = bsp_1 - bsp_2
    
    return bsp

def black_scholes_parity(stock, strike, rfi, delta, time, sigma):
    
    put = black_scholes_put(stock, strike, rfi, delta, time, sigma)
    call = black_scholes_call(stock, strike, rfi, delta, time, sigma)
    call += strike * exp(-rfi * time) - stock * exp(-delta * time)
    
    print("Call = " + str(call))
    print("Put = " + str(put))
    
    if put == call:
        print("Put-call parity holds")
    else:
        print("Put-call parity does not hold")

# given test case
black_scholes_parity(250,260,.04,.02,.5,.2)