# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:41:26 2020

@author: marsh
"""

import csv
import pandas as pd

read_file = pd.read_excel (r'C:\Users\marsh\OneDrive\Desktop\Project #2\Excel\Project #2 Data.xlsx', sheet_name='ADP')
read_file.to_csv (r'C:\Users\marsh\OneDrive\Desktop\Project #2\Code\ADP.csv', index = None, header=True)

read_file = pd.read_excel (r'C:\Users\marsh\OneDrive\Desktop\Project #2\Excel\Project #2 Data.xlsx', sheet_name='LMT')
read_file.to_csv (r'C:\Users\marsh\OneDrive\Desktop\Project #2\Code\LMT.csv', index = None, header=True)

read_file = pd.read_excel (r'C:\Users\marsh\OneDrive\Desktop\Project #2\Excel\Project #2 Data.xlsx', sheet_name='AIR')
read_file.to_csv (r'C:\Users\marsh\OneDrive\Desktop\Project #2\Code\AIR.csv', index = None, header=True)


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

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')