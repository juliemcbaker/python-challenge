#PyBank Assignment
#Julie Baker
#May 2021

import os
import csv
import operator

# need to read in PyBank/Resources/budget_data.csv
budget_csv = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_data.csv")
# creating a filepath for a second file that sets as a dictionary 
#.budget_working = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_working.csv")

# function to create a list of monthly changes which will be used to calculate average change
#.change_list = []

#. def monthly_change(row):
#.    this_row = (row)
#.    last_row = (row-1)
#.    this_month = (this_row['Profit/Losses'])
#.    last_month = (last_row['Profit/Losses'])
#.    this_change = this_month - last_month
#.    change_list.append(this_change)

with open(budget_csv) as csv_file:            
    csv_reader = csv.reader(csv_file, delimiter = ',')
    dict_data = csv.DictReader(csv_file, delimiter = ',')
    months = 0 
    net_total = 0 
    highest_value = 0
    lowest_value = 0
    change_list = []

    for row in dict_data:
            # counts number of months
        months = months + 1
            # calculates overall profit/loss for entire period
        net_total = int(row['Profit/Losses']) + net_total

        #.if row == 1:
        #.    start_value = int(row['Profit/Losses'])
        #. else:
        #    start_value = start_value    
        
        # identifies highest & lowest values & corresponding months
        if int(row['Profit/Losses']) > highest_value:
            highest_value = int(row['Profit/Losses'])
            highest_month = (row['Date'])
        elif int(row['Profit/Losses']) < lowest_value:
            lowest_value = int(row['Profit/Losses'])
            lowest_month = (row['Date'])
        else:
            next
        
      #.  if int(row['Profit/Losses']) != start_value:
      #.      this_row = (row)
      #.      last_row = (row-1)
      #.      this_month = (this_row['Profit/Losses'])
      #.      last_month = (last_row['Profit/Losses'])
      #.      this_change = this_month - last_month
      #.      change_list.append(this_change)
      #.  print(change_list)

# starting a write file to create dictionary
#.    with open(budget_working, mode='w') as outfile:
#.        writer = csv.writer(outfile)
#.        mydict = {rows[0]:rows[1] for rows in csv_reader}
    
        #.if row != 1:
        #.    total_change = total_change + int(row[1])
#.        writer(mydict)
  #  next(csv_reader, None)
   # for row in csv_reader:

# Pt1: calculate changes in "Profits/Losses" over the entire period
    # does this mean each month-to-month shift?
    # if so, probably makes sense to write this info somewhere for holding
        # possible holding location (PyBank/Analysis/interim.csv); consider zip method
        # will need to pull from it to do next part
# Pt2: find the average of those changes
#..avg_change = averages from above


# Analysis should print in terminal 
print('Financial Analysis')
print("-------------------------")
print("Total Months: " + str(months)) 
print("Total: $" + str(net_total))
#    print("Average Change: $" + avg_change)
print("Greatest Increase in Profits: " + str(highest_month) + " ($" + str(highest_value) + ")")
print("Greatest Decrease in Profits: " + str(lowest_month) + " ($" + str(lowest_value) + ")")

# Analysis should export to text (PyBank/Analysis/budget_result.txt)
output_path = os.path.join(os.getcwd(), 'PyBank', 'Analysis', 'budget_result.txt')

# opens file 
a = open(output_path, 'w+')
# writes header
a.write("Financial Analysis")
a.write('\n')
a.write("------------------------")
a.write('\n')       
#writes output & pulls from variables to input values
a.write(f"Total Months: {months}")
a.write('\n')       
a.write(f"Total: ${net_total}")
a.write('\n')       
#.a.write(f"Average Change: $ + {avg_change}")
a.write('\n')       
a.write(f"Greatest Increase in Profits: {highest_month} (${highest_value})")
a.write('\n')       
a.write(f"Greatest Decrease in Profits: {lowest_month} (${lowest_value})")
a.close()