
# Importing Modules/Dependencies
import os 
import csv

# creating the path to the Resource folder to grab the csv file.
csvpath = os.path.join('Resources', 'budget_data.csv')

# setting up list to hold data
months = []
profit = []

#loop through the budget_data csv file and add it to the list variables months and profit
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit.append(float(row[1]))

#calculating data in in the month and profit list to report on financials. 
total_months = len(months)
profit_total = int(sum(profit))
profit_change = [profit[i] - profit[i - 1] for i in range(1, len(profit))]
avg_profit = round(sum(profit_change) / len(profit_change), 2)
max_profit = max(profit_change)
min_profit = min(profit_change)

#summary write-up to be printed in terminal. 
summary = (
    "Financial Analysis\n"
    "____________________________\n"
    f"Total Months: {total_months}\n"
    f"Profit Total: ${profit_total:,.0f}\n"
    f"Average Change: ${avg_profit:,.2f}\n"
    f"Greatest Increase in Profit: ${max_profit:,.0f}\n"
    f"Greatest Loss in Profit: ${min_profit:,.0f}\n"
    "____________________________"
)

print(summary)

#writing write-up to a txt file. 
with open(os.path.join("Analysis", "financeResults.txt"), "w+") as bankAnalysis_text:
    bankAnalysis_text.write(summary)