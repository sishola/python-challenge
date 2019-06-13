# Import dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    VoterID = []
    County = []
    Candidate = []

#read contents of the file
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])


#get total votes
total_votes = len(VoterID)


#count votes
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

for i in range(total_votes):
    if Candidate[i] == "Khan":
        khan_votes = khan_votes + 1
    if Candidate[i] == "Correy":
        correy_votes = correy_votes + 1
    if Candidate[i] == "Li":
        li_votes = li_votes + 1
    if Candidate[i] == "O'Tooley":
        otooley_votes = otooley_votes + 1
        

#analyse votes
winner_vote_count = max(khan_votes,correy_votes,li_votes,otooley_votes)
if khan_votes == winner_vote_count:
    winner = "Khan"
elif correy_votes == winner_vote_count:
    winner = "Correy"
elif li_votes == winner_vote_count:
    winner = "Li"
else:
    winner = "O'Tooley"

#print out results to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {(khan_votes*100)/total_votes:.3f}% ({khan_votes})")
print(f"Correy: {(correy_votes*100)/total_votes:.3f}% ({correy_votes})")
print(f"Li: {(li_votes*100)/total_votes:.3f}% ({li_votes})")
print(f"O'Tooley: {(otooley_votes*100)/total_votes:.3f}% ({otooley_votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")


#write to output file
#write to output file
output_file = os.path.join("Output","poll_analysis.txt")

writer = open(output_file,"w")

writer.write(f"Election Results")
writer.write(f"-------------------------")
writer.write(f"Total Votes: {total_votes}")
writer.write(f"-------------------------")
writer.write(f"Khan: {(khan_votes*100)/total_votes:.3f}% ({khan_votes})")
writer.write(f"Correy: {(correy_votes*100)/total_votes:.3f}% ({correy_votes})")
writer.write(f"Li: {(li_votes*100)/total_votes:.3f}% ({li_votes})")
writer.write(f"O'Tooley: {(otooley_votes*100)/total_votes:.3f}% ({otooley_votes})")
writer.write(f"-------------------------")
writer.write(f"Winner: {winner}")
writer.write(f"-------------------------")