
# Election Results Analysis

## Overview

This simple Python script reads a CSV file containing election data and calculates the total number of votes, the percentage of votes for each candidate, and the winner of the election. The script outputs the election results to the console and saves them to a text file.

## Requirements

To run this script, you need Python 3.x and the CSV file `election_data.csv` stored in a folder named "Resources". You should also have a folder called "Analysis" to store a text file. The file structure requirments are already setup if you clone the repository.

## Usage

1. Clone this repository.
2. Ensure the "Resources" folder containing the `election_data.csv` file is in the same directory as the script.
3. Open your preferred terminal and navigate to the directory containing the `pollingResults.py` script.
4. Run the script by typing `python pollingResults.py` and pressing Enter.

After running the script, you will see the election results displayed in the console. Additionally, a text file named `pollAnalysis.txt` containing the election results will be created in a folder named "Analysis" in the same directory.

## Election Data Format

The election data in the CSV file should have the following format:

```
Ballot ID,County,Candidate
123456,SomeCounty,John Doe
234567,AnotherCounty,Jane Smith
345678,AnotherCounty,Pat Gray
```

## Output

The script outputs the following election results:

* Total Votes: The total number of votes in the election
* A list of candidates with their respective vote percentage and total vote count
* The winner of the election

The output will have the following format:

```
Election Results
____________________________
Total Votes: 1,000,000
____________________________
Jane Smith: 50.00% (500,000)
John Doe: 20.00% (200,000)
Pat Gray: 30.00% (300,000)
____________________________
Winner: Jane Smith
```

## Customization

To analyze a different election dataset, simply replace the `election_data.csv` file in the "Resources" folder with your own CSV file following the same format as described in the "Election Data Format" section. Make sure the new file is named `election_data.csv` or update the `csvpath` variable in the script to match the new file name.

---



# Budget Data Analysis

## Overview

This Python script reads a CSV file containing budget data and calculates the total number of months, the net total amount of profit/losses, the average change in profit/losses, the greatest increase in profits, and the greatest decrease in losses. The script outputs the financial analysis to the console and saves it to a text file.

## Requirements

To run this script, you need Python 3.x and the CSV file `budget_data.csv` stored in a folder named "Resources". You should also have a folder called "Analysis" to store a text file. The file structure requirments are already setup if you clone the repository.

## Usage

1. Clone this repository or download the script `financialResults.py` to your local machine.
2. Ensure the "Resources" folder containing the `budget_data.csv` file is in the same directory as the script.
3. Open a terminal (Command Prompt, PowerShell, or Terminal) and navigate to the directory containing the script.
4. Run the script by typing `python financialResults.py` and pressing Enter.

After running the script, you will see the financial analysis displayed in the console. Additionally, a text file named `financeResults.txt` containing the financial analysis will be created in a folder named "Analysis" in the same directory as the script.

## Budget Data Format

The budget data in the CSV file should have the following format:

```
Date,Profit/Losses
Jan-2010,867884
Feb-2010,984655
```

## Output

The script outputs the following financial analysis:

* Total Months: The total number of months in the dataset
* Profit Total: The net total amount of profit/losses
* Average Change: The average change in profit/losses over the entire period
* Greatest Increase in Profit: The maximum increase in profit from one month to the next
* Greatest Loss in Profit: The maximum decrease in profit from one month to the next

The output will have the following format:

```
Financial Analysis
____________________________
Total Months: 42
Profit Total: $34,567,891
Average Change: $-2,345.67
Greatest Increase in Profit: $1,234,567
Greatest Loss in Profit: $-2,345,678
```

## Customization

Follow the same instructions as above.
