import os

import csv
csvpath = os.path.join('Resources', 'election_data.csv')
election_results = open(csvpath)

total = 0

for row in election_results:
    #when printing print(total - 1) to remove header count
    total += 1
# find how to locate names of all candidates

# nested loop to show votes for each canditdate

# show the winner; percent of votes; (total votes recieved)







