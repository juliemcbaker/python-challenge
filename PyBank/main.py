#PyBank Assignment
#Julie Baker
#May 2021

import os
import csv
import operator

# need to read in PyBank/Resources/budget_data.csv
budget_csv = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_data.csv")

with open(budget_csv) as csv_file:            
    csv_reader = csv.reader(csv_file, delimiter = ',')
    dict_data = csv.DictReader(csv_file, delimiter = ',')
    months = 0 
    net_total = 0 
    highest_value = 0
    lowest_value = 0

    for row in dict_data:
        # counts number of months
        months = months + 1
        # calculates overall profit/loss for entire period
        net_total = int(row['Profit/Losses']) + net_total
        # identifies highest & lowest values & corresponding months
        if int(row['Profit/Losses']) > highest_value:
            highest_value = int(row['Profit/Losses'])
            highest_month = (row['Date'])
        elif int(row['Profit/Losses']) < lowest_value:
            lowest_value = int(row['Profit/Losses'])
            lowest_month = (row['Date'])
        else:
            next

# Code to determine month-to-month change, saves each value to a list, computes average from the list
with open(budget_csv) as csv_file:            
    dict_data2 = csv.DictReader(csv_file, delimiter = ',')
    change_list = []
    row_num = 0

    for row in dict_data2:
        row_num = row_num + 1
        
        if row_num == 1:
            prev_row = row
        else:
            this_row = row
            this_month = int(this_row['Profit/Losses'])
            last_month = int(prev_row['Profit/Losses'])
            this_change = this_month - last_month
            change_list.append(this_change)
            prev_row = row
        
    avg_change = ("{0:.2f}".format(sum(change_list)/(months-1)))
    print(avg_change)

# Analysis should print in terminal 
print('Financial Analysis')
print("-------------------------")
print(f"Total Months: {months}") 
print(f"Total: $ {net_total}")
print(f"Average Change: $ {avg_change}")
print(f"Greatest Increase in Profits: {highest_month} ($ {highest_value})")
print(f"Greatest Decrease in Profits: {lowest_month} ($ {lowest_value})")

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
a.write(f"Average Change: $ + {avg_change}")
a.write('\n')       
a.write(f"Greatest Increase in Profits: {highest_month} (${highest_value})")
a.write('\n')       
a.write(f"Greatest Decrease in Profits: {lowest_month} (${lowest_value})")
a.close()