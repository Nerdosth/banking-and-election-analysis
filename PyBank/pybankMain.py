
# Importing Modules/Dependencies
import os  #ensures code can work on multiple OS systems 
import csv

# creating the path
csvpath = os.path.join('Resources', 'budget_data.csv')

# setting up variables to hold data
months = []
profit = []
profit_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_data_header = next(csvfile)

#loop through the budget_data csv file and add it to the list variables months and profit
    for row in csvreader:
        months.append(row[0])
        profit.append(float(row[1]))
    profit_total = int(sum(profit)) #setting up this variable to be formatted as a dollar value when printing

#loop through data to calculate the greatest increase and decrease of profit

    for value in range(1,len(profit)):
        profit_change.append(profit[value] - profit[value-1])
        avg_profit = round(sum(profit_change)/len(profit_change),2)
        max_profit = max(profit_change)
        min_profit = min(profit_change)
        total_months = (len(months)) #adds all the months up for printing

#Summary of the data analyzed from the cvs file. 
print("Financial Analysis") 
print("____________________________\n") #/n inserts another line between visual break between report title and data
print(f"Total Months: {total_months}") 
print("Profit Total: ${:0,.0f}".format(profit_total)) #{:0,.2f}".format is used to format the print out to include commas for thousands
print("Average Change: ${:0,.2f}".format(avg_profit))
print("Greatest Increase in Profit: ${:0,.0f}".format(max_profit))
print("Greatest Loss in Profit: ${:0,.0f}".format(min_profit))

#write printed data to text file titled bankAnalysis.txt
with open(os.path.join("Analysis","bankAnalysis.txt"), "w+") as bankAnalysis_text:
    bankAnalysis_text.write("Financial Analysis\n") 
    bankAnalysis_text.write("____________________________\n") #/n needed at the end of each "" to prompt a new line
    bankAnalysis_text.write(f"Total Months: {total_months}\n") 
    bankAnalysis_text.write("Profit Total: ${:0,.0f}\n".format(profit_total))
    bankAnalysis_text.write("Average Change: ${:0,.2f}\n".format(avg_profit))
    bankAnalysis_text.write("Greatest Increase in Profit: ${:0,.0f}\n".format(max_profit))
    bankAnalysis_text.write("Greatest Loss in Profit: ${:0,.0f}\n".format(min_profit))
