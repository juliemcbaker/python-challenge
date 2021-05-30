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

with open(budget_csv) as csv_file:            
    csv_reader = csv.reader(csv_file, delimiter = ',')
    dict_data = csv.DictReader(csv_file, delimiter = ',')
    months = 0 
    net_total = 0

    # this is the one converted to dictionary
    highest_value = 0
    lowest_value = 0
    for row in dict_data:
        # counts number of months
        months = months + 1
        # calculates overall profit/loss for entire period
        net_total = float(row['Profit/Losses']) + net_total
        if float (row['Profit/Losses']) > highest_value:
            highest_value = float(row['Profit/Losses'])
            highest_month = (row['Date'])
        elif float(row['Profit/Losses']) < lowest_value:
            lowest_value = float(row['Profit/Losses'])
            lowest_month = (row['Date'])
        else:
            next

    print(highest_value)
    print(highest_month)
    print(lowest_value)
    print(lowest_month)

    # this is the standard csv; trying based on stackoverflow to change the header
#.    with open(budget_working, mode='w') as outfile:
  #.      writer = csv.writer(outfile)
    #.    for row in csv_reader:
      #.      newHeader = csv.writer(outfile)
        #.    newFN = ['Date', 'Up_Down']
          #.  newHeader.writerow(newFN)
         #.   print(row)

#. print(outfile)

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
# based on code found on stackoverflow.com
#max_value = max(dummy('Profit/Losses'))
# max_keys = [dict.items('Date') if dict.values(Profit/Losses) == max_value]
#, key=Date.get)
#print(max_value)
#print(max_keys)

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
#.print(f'Financial Analysis')  --UNSURE WHY KEEP GETTING SYNTAX ERROR ON THIS & NEXT LINE
#.print("-------------------------")
print("Total Months: " + str(months)) 
print("Total: $" + str(net_total))
#    print("Average Change: $" + avg_change)
print("Greatest Increase in Profits: " + str(highest_month) + " ($" + str(highest_value) + ")")
print("Greatest Decrease in Profits: " + str(lowest_month) + " ($" + str(lowest_value) + ")")

# Analysis should export to text (PyBank/Analysis/budget_result.txt)
#.output_path = os.path.join(os.getcwd(), 'PyBank', 'Analysis', 'budget_result.txt')

# found tip about append & read at geeksforgeeks.org
#.with open(output_path, 'a+') as text:
    # initializes the writerls
 #.   text_out = text.write(output_path)
    
    #writes header
    #.text_out ("Financial Analysis")
    #.text_out.write ("-------------------------")
    
    #writes output & pulls from variables to input values
    #.text_out.writerow("Total Months: " + months)
  #.  text_out.writerow("Total: $" + net_total)
  #.  text_out.writerow("Average Change: $" + avg_change)
  #.  text_out.writerow("Greatest Increase in Profits: " + high_time + " ($" + high_money + ")")
  #.  text_out.writerow("Greatest Decrease in Profits: " + low_time + " ($" + low_money + ")")