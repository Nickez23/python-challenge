#Import os
import os

#import csv reader
import csv
from statistics import mean

csvpath = os.path.join('Resources', 'budget_data.csv')
financial_analysis = open(csvpath)

total = 0
month = 0
net_total = 0
pre_prof = 0
changes = 0
average_changes = 0
greatest_profit = 0
lowest_profit = 0

for row in financial_analysis:
    month += 1
    total = int(row['Profit/Losses'])
    net_total += total
    changes = net_total - pre_prof
    average_changes = mean(changes)
    #use max and min func

output = f'''
Financial Analysis
----------------------------
Total months: {month}
Total: {net_total:,.2f}
Average Change: {average_changes}

'''

print(output)








