# PyPoll
# Julie Baker
# May-June 2021

import os
import csv

# read in csv & convert to a dictionary
# need to read in PyPoll/Resources/election_data.csv
# created smaller file PyPoll/Resources/election_test.csv for testing
polling_csv = os.path.join(os.getcwd(), "PyPoll", "Resources", "election_data.csv")
## MAKE SURE THIS IS UPDATED TO BE THE FINAL FILE
# # creating a filepath for a second file that sets as a dictionary 
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

# Reordering of candidates by votes received for output
# This loop determines WINNER
if cand_1_counter > cand_2_counter:
    hold1_cand = cand_2
    hold1_count = cand_2_counter
    second_count = 0
    if cand_1_counter > cand_3_counter:
        hold2_cand = cand_3
        hold2_count = cand_3_counter
        if cand_1_counter > cand_4_counter:
            winner = cand_1
            winner_count = cand_1_counter
            hold3_cand = cand_4
            hold3_count = cand_4_counter
        else:
            second_place = cand_1
            second_count = cand_1_counter
            winner = cand_4
            winner_count = cand_4_counter
    elif cand_3_counter > cand_4_counter:
        hold2_cand = cand_1
        hold2_count = cand_1_counter
        winner = cand_3
        winner_count = cand_3_counter
        hold3_cand = cand_4
        hold3_count = cand_4_counter
elif cand_2_counter > cand_3_counter:
    hold1_cand = cand_1
    hold1_count = cand_1_counter
    hold2_cand = cand_3
    hold2_count = cand_3_counter
    if cand_2_counter > cand_4_counter:
        winner = cand_2
        winner_count = cand_2_counter
        hold3_cand = cand_4
        hold3_count = cand_4_counter
        
# This loop to determines 2nd, 3rd, & 4th places
if second_count > 0:
    if hold1_count > hold2_count:
        third_place = hold1_cand
        third_count = hold1_count
        fourth_place = hold2_cand
        fourth_count = hold2_cand
    else:
        third_place = hold2_cand
        third_count = hold2_count
        fourth_place = hold1_cand
        fourth_count = hold1_count
elif hold1_count > hold2_count:
    if hold1_count > hold3_count:
        second_place = hold1_cand
        second_count = hold1_count
        if hold2_count > hold3_count:
            third_place = hold2_cand
            third_count = hold2_count
            fourth_place = hold3_cand
            fourth_count = hold3_count
        else:
            third_place = hold3_cand
            third_count = hold3_count
            fourth_place = hold2_cand
            fourth_count = hold2_count
    elif hold3_count > hold2_count:
        second_place = hold3_cand
        second_count = hold3_count
        third_place = hold2_cand
        third_count = hold2_count
        fourth_place = hold1_cand
        fourth_count = hold1_count
elif hold1_count > hold3_count:
    second_place = hold2_cand
    second_count = hold2_count
    third_place = hold1_cand
    third_count = hold1_count
    fourth_place = hold3_cand
    fourth_count = hold3_count

# calculate percentage of votes for each candidate
winner_percent = "{:.3f}".format((winner_count/total_votes)*100)
second_percent = "{:.3f}".format((second_count/total_votes)*100)
third_percent = "{:.3f}".format((third_count/total_votes)*100)
fourth_percent = "{:.3f}".format((fourth_count/total_votes)*100)

# Output for terminal
# ================================================================
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
print(f'{winner}: {winner_percent}% ({winner_count})') 
print(f'{second_place}: {second_percent}% ({second_count})') 
print(f'{third_place}: {third_percent}% ({third_count})') 
print(f'{fourth_place}: {fourth_percent}% ({fourth_count})') 
print("----------------------------")
print("Winner: " + str(winner))
print("----------------------------")

# ALSO PRINT TO TEXT FILE