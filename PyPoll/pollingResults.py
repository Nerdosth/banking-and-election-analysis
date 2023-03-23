import os
import csv

# creating the path to the Resource folder to grab the csv file.
csvpath = os.path.join('Resources', 'election_data.csv')

# setting up dictionary to store vote count
votes = {}

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # skip header

    # Loop through the CSV file
    for row in csvreader:
        # extracts the candidate's name from the row
        candidate = row[2]
        
        # Check if the candidate is not in the votes dictionary
        if candidate not in votes:
            # Initialize the candidate's vote count to 0
            votes[candidate] = 0
        
        # Increment the vote count for the candidate
        votes[candidate] += 1

# Calculate the total number of votes
total_votes = sum(votes.values())

# Setting up list to hold vote results 
results = []

# Loop through each candidate and their vote count in the votes dictionary
for candidate, vote_count in votes.items():
    # Calculate the vote percentage for the candidate
    vote_percent = round((vote_count / total_votes) * 100, 2)
    
    # Append the formatted result for the candidate to the results list
    results.append(f"{candidate}: {vote_percent:.2f}% ({vote_count:,.0f})")

# Create a summary string of the election results
summary = (
    "Election Results\n"
    "____________________________\n"
    f"Total Votes: {total_votes:,.0f}\n"
    "____________________________\n" +
    "\n".join(results) +
    "\n____________________________\n"
    f"Winner: {max(votes, key=votes.get)}\n"
)

# Print the summary to the console
print(summary)

# Write the summary to a text file called pollAnalysis.txt
with open(os.path.join("Analysis", "pollAnalysis.txt"), "w+") as pollAnalysis_text:
    pollAnalysis_text.write(summary)
