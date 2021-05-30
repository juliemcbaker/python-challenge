# PyPoll
# Julie Baker
# May-June 2021

import os
import csv

# read in csv & convert to a dictionary
# need to read in PyPoll/Resources/election_data.csv
# created smaller file PyPoll/Resources/election_test.csv for testing
polling_csv = os.path.join(os.getcwd(), "Resources", "election_test.csv")
# creating a filepath for a second file that sets as a dictionary 
polls_working = os.path.join(os.getcwd(), "Resources", "election_working.csv")

with open(polling_csv) as csv_file:            
    csv_reader = csv.reader(csv_file, delimiter = ',')
    dummy = csv.DictReader(csv_file, delimiter = ',')


# get vote count
    # this is the one converted to dictionary
    out_dummy = []
    for row in dummy:
        print(row)
        if 'Candidate' not in [out_dummy]:
           out_dummy.append(row['Candidate'])
           out_dummy.append("BLUE")
        else:
            next
    print(out_dummy)      

# generate list of candidates
    # this is standard csv
#.    output_list = []
  #.  for thisrow in csv_reader:
    #.    print(thisrow)
      #.  if [thisrow[2]] not in output_list:
        #.    output_list.append[thisrow[2]]
        #.    print("what's wrong with this syntax?")
        #.    print(output_list)


# calculate total number of votes for each candidate

# calculate percentage of votes for each candidate

# popular vote winner

# ================================================================
# print("Election Results")
# print("----------------------------")
# print("Total Votes: " + total_votes)
# print("----------------------------")
# print {name1}: percent_name1  (total_name1)
# etc for each name
# print("----------------------------")
# print("Winner: " + winner)
# print("----------------------------")

# ALSO PRINT TO TEXT FILE