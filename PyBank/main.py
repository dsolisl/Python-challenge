import os
import csv
total_months = 0
total_profit = 0
initial_profit = 0
change_profit = 0
sum_change_profit = 0
avg_profit_change = 0 
highest_profit = 0
date_high = ""
date_low = ""
lowest_profit = 0

initial_data = 'Resources/budget_data.csv'

with open(initial_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        total_months +=  1

        total_profit += int(row[1])

        if total_months == 1:
            initial_profit = int(row[1])

        else: 
            change_profit =int(row[1]) - initial_profit
            if change_profit > highest_profit:
                highest_profit = change_profit
                date_high = row[0]
            if change_profit <lowest_profit:
                date_low = row[0]
                lowest_profit = change_profit 
            sum_change_profit +=change_profit
            initial_profit = int(row[1])
            
avg_profit_change = sum_change_profit/(total_months -1)

output_path = 'Resources/summary_profit.txt'

with open(output_path, 'w') as txt_file:
    print("Financial Analyis", file = txt_file)
    print("-"*10, file = txt_file)
    print(f"Total months: {total_months}", file = txt_file)
    print(f"Total: {total_profit}", file = txt_file)
    print(f"Average change: $ {avg_profit_change}", file = txt_file)
    print(f"Greatest Increase in Profits: {date_high} (${highest_profit}) ", file = txt_file)
    print(f"Greatest Decrease in Profits:{date_low} (${lowest_profit} )", file = txt_file )



print("Financial Analyis")
print("-"*10)
print(f"Total months: {total_months}")
print(f"Total: {total_profit}")
print(f"Average change: $ {avg_profit_change}")
print(f"Greatest Increase in Profits: {date_high} (${highest_profit}) ")
print(f"Greatest Decrease in Profits:{date_low} (${lowest_profit} )" )
