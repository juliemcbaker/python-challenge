# PyPoll
# Julie Baker
# May-June 2021

import os
import csv

# read in csv & convert to a dictionary
# need to read in PyPoll/Resources/election_data.csv
# created smaller file PyPoll/Resources/election_test.csv for testing
polling_csv = os.path.join(os.getcwd(), "PyPoll", "Resources", "election_test.csv")
# creating a filepath for a second file that sets as a dictionary 
polls_working = os.path.join(os.getcwd(), "PyPoll", "Resources", "election_working.csv")

with open(polling_csv) as csv_file:            
    csv_reader = csv.reader(csv_file, delimiter = ',')
    dummy = csv.DictReader(csv_file, delimiter = ',')

# vote count function
def vote_count()

# get vote count
    total_votes = 0
    # this is the one converted to dictionary
    out_dummy = []
    for row in dummy:
        print(row)
        total_votes = total_votes + 1   # works correctly
        if row['Candidate'] not in out_dummy:
           out_dummy.append(row['Candidate'])

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
    # use out_dummy from above (once it works), to set-up counters for each person
    # iterate through data with conditionals that increase counters

# calculate percentage of votes for each candidate
    # use results from previous 

# popular vote winner
    # winner = max[counters] ## conceptul


# ================================================================
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
# print {name1}: percent_name1  (total_name1)
# etc for each name
# print("----------------------------")
# print("Winner: " + str(winner))
# print("----------------------------")

# ALSO PRINT TO TEXT FILE