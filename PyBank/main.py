#PyBank Assignment
#Julie Baker
#May 2021

import os
import csv

# need to read in PyBank/Resources/budget_data.csv
budget_csv = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_data.csv")

with open(budget_csv) as csv_file:            
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    for row in csv_reader:
        print(row)
  
  #  next(csv_reader, None)
   # for row in csv_reader:
        
# need to count the number of months in the dataset
    # should be something like count rows - 1 (to account for header)
months = row.index
print (months)

# calculate net total amount of "Profits/Losses" for entire period
    # sum everything in column B/2
#..net_total = sum(col.2)

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
#    print("Financial Analysis")
#    print("-------------------------")
#    print("Total Months: " + months)
#    print("Total: $" + net_total)
#    print("Average Change: $" + avg_change)
#    print("Greatest Increase in Profits: " + high_time + " ($" + high_money + ")"
#    print("Greatest Decrease in Profits: " + low_time + " ($" + low_money + ")"

# Analysis should export to text (PyBank/Analysis/budget_result.txt)
#.output_path = os.path.join(os.getcwd(), 'Analysis', 'budget_result.txt')

#.with open(output_path, 'w') as text:
    # initializes the writerls
   #. text_out = text.writer(text, delimiter=',')
    
    #writes header
  #.  text_out.writerow("Financial Analysis")
  #.  text_out.writerow("-------------------------")
    
    #writes output & pulls from variables to input values
  #.  text_out.writenow("Total Months: " + months)
  #.  text_out.writenow("Total: $" + net_total)
  #.  text_out.writenow("Average Change: $" + avg_change)
  #.  text_out.writenow("Greatest Increase in Profits: " + high_time + " ($" + high_money + ")")
  #.  text_out.writenow("Greatest Decrease in Profits: " + low_time + " ($" + low_money + ")")
                       
   