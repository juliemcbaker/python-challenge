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
    dict_reader = csv.DictReader(csv_file, delimiter = ',')

# initiatate vote counters
    total_votes = 0
    cand_1_counter = 0
    cand_2_counter = 0
    cand_3_counter = 0
    cand_4_counter = 0
    
    # creates list of candidates & accumulates total votes
    candidates = []
    for row in dict_reader:
        print(row)
        total_votes = total_votes + 1   
        if row['Candidate'] not in candidates:
           candidates.append(row['Candidate'])
        
        # accumulates totals for each candidate
        if row['Candidate'] == candidates[0]:
            cand_1 = candidates[0]
            cand_1_counter = cand_1_counter + 1
        elif row['Candidate'] == candidates[1]:
            cand_2 = candidates[1]
            cand_2_counter = cand_2_counter + 1
        elif row['Candidate'] == candidates[2]:
            cand_3 = candidates[2]
            cand_3_counter = cand_3_counter + 1
        elif row['Candidate'] == candidates[3]:
            cand_4 = candidates[3]
            cand_4_counter = cand_4_counter +1
        else:
            next

    print(candidates)

   
    print(cand_1, cand_1_counter)
    print(cand_2, cand_2_counter)
    print(cand_3, cand_3_counter)
    print(cand_4, cand_4_counter)

# create reordering of candidates by number of votes received for output

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