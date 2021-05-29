#PyBank Assignment
#Julie Baker
#May 2021

import os
import csv

# need to read in PyBank/Resources/budget_data.csv
budget_csv = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_data.csv")
# creating a filepath for a second file that sets as a dictionary 
budget_working = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_working.csv")

with open(budget_csv) as csv_file:            
    csv_reader = csv.DictReader(csv_file, delimiter = ',')
    dummy = csv.DictReader(csv_file, delimiter = ',')
    months = 0 
    net_total = 0    

    for row in csv_reader:
        print(row)
        # counts number of months
        months = months + 1
        # calculates overall profit/loss for entire period
        net_total = float(row['Profit/Losses']) + net_total

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

# Greatest increase in profits (date & amount) from entire period
#..high_time; high_money

# Greatest decrease in losses (date & amount) from entire period
#..low_time; low_money

# Analysis should be
    # Financial Analysis
    # ------------------------
    # Total Months: xxx
    # Total: $xxxxxxx
    # Average Change: $
    # Greatest Increase in Profits: Month-YEAR ($.....)
    # Greatest Decrease in Profits: Month-YEAR ($.....)

# Analysis should print in terminal 
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(net_total))
#    print("Average Change: $" + avg_change)
#    print("Greatest Increase in Profits: " + high_time + " ($" + high_money + ")"
#    print("Greatest Decrease in Profits: " + low_time + " ($" + low_money + ")"

# Analysis should export to text (PyBank/Analysis/budget_result.txt)
output_path = os.path.join(os.getcwd(), 'PyBank', 'Analysis', 'budget_result.txt')

# found tip about append & read at geeksforgeeks.org
with open(output_path, 'a+') as text:
    # initializes the writerls
    text_out = text.write(output_path)
    
    #writes header
    #.text_out ("Financial Analysis")
    #.text_out.write ("-------------------------")
    
    #writes output & pulls from variables to input values
    #.text_out.writerow("Total Months: " + months)
  #.  text_out.writerow("Total: $" + net_total)
  #.  text_out.writerow("Average Change: $" + avg_change)
  #.  text_out.writerow("Greatest Increase in Profits: " + high_time + " ($" + high_money + ")")
  #.  text_out.writerow("Greatest Decrease in Profits: " + low_time + " ($" + low_money + ")")
                       
   