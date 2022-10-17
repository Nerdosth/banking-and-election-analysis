# Importing Modules/Dependencies
import os  #ensures code can work on multiple OS systems 
import csv

# creating the path
csvpath = os.path.join('Resources', 'election_data.csv')

# setting up variables to hold data
unique_votes = []
candidate_list = []
Stockham_count = []
Degette_count = []
Doane_count = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_data_header = next(csvfile)

#loop through the election_data csv file and add it to the list variables votes and candidates
    for row in csvreader:
       unique_votes.append(row[0])
       candidate_list.append(row[2])

#counting up the total votes received during the election
total_votes = len(unique_votes)

#counting up the total votes each candidate received 
for candidate in candidate_list:
    if candidate == "Charles Casper Stockham":
            Stockham_count.append(candidate)
            Stockham_votes = len(Stockham_count)
    elif candidate == "Diana DeGette":
             Degette_count.append(candidate)
             Degette_votes = len(Degette_count)
    else: #counting up Doane's votes
             Doane_count.append(candidate)
             Doane_votes = len(Doane_count)

#calculate the percentage of canidate votes against the total votes 
Stockham_percent = round((Stockham_votes/total_votes)*100,2)
Degette_percent = round((Degette_votes/total_votes)*100,2)
Doane_percent = round((Doane_votes/total_votes)*100,2)

#print out summary

print("Election Results") 
print("____________________________\n")
print("Total Votes:", "{:0,.0f}".format(total_votes))
print("____________________________\n")
print(Stockham_count[0],":", "{:.2%}".format((Stockham_percent)/100), "({:0,.0f})".format((Stockham_votes)))
print(Degette_count[0],":", "{:.2%}".format((Degette_percent)/100), "({:0,.0f})".format((Degette_votes)))
print(Doane_count[0],":", "{:.2%}".format((Doane_percent)/100), "({:0,.0f})".format((Doane_votes)))

#determine who won with a python code and print out the results
print("____________________________\n")
if Stockham_votes > Degette_votes and Stockham_votes > Doane_votes:
    print("Winner:" , Stockham_count[0])
elif Degette_votes > Stockham_votes and Degette_votes > Doane_votes:
    print("Winner:" , Degette_count[0])
elif Doane_votes > Degette_votes and Doane_votes> Stockham_votes:
    print("Winner:" , Doane_count[0])

#write summary to text file 
with open(os.path.join("Analysis","pollAnalysis.txt"), "w+") as pollAnalysis_text:
    pollAnalysis_text.write("Election Results\n") 
    pollAnalysis_text.write("____________________________\n")
    pollAnalysis_text.write("Total Votes: {:0,.0f}\n".format(total_votes))
    pollAnalysis_text.write("____________________________\n")
    pollAnalysis_text.write(Stockham_count[0]+": "+ "{:.2%}".format((Stockham_percent)/100)+" "+ "({:0,.0f})\n".format((Stockham_votes))) #for printing I had to replace , with + to concatenate to avoid an multiple argument error
    pollAnalysis_text.write(Degette_count[0]+": "+ "{:.2%}".format((Degette_percent)/100)+" "+ "({:0,.0f})\n".format((Degette_votes)))
    pollAnalysis_text.write(Doane_count[0]+": "+ "{:.2%}".format((Doane_percent)/100)+" "+ "({:0,.0f})\n".format((Doane_votes)))

#determine who won with a python code and write out the results
    pollAnalysis_text.write("____________________________\n")
    if Stockham_votes > Degette_votes and Stockham_votes > Doane_votes:
        pollAnalysis_text.write(f"Winner: {Stockham_count[0]}")
    elif Degette_votes > Stockham_votes and Degette_votes > Doane_votes:
        pollAnalysis_text.write(f"Winner: {Degette_count[0]}")
    elif Doane_votes > Degette_votes and Doane_votes> Stockham_votes:
        pollAnalysis_text.write(f"Winner: {Doane_count[0]}")

