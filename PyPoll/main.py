### Main Script to run each analysis
import os
import csv

# Set the file path
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        total_votes += 1

        if candidate not in candidates:
            candidates.append(candidate)

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Initialize variables for winner information
winner = ""
winning_votes = 0

# Print election results in cmd
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through candidates
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100

    # Determine the winner
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

# label results location
output_path = os.path.join("PyPoll", "analysis", "output_election_data.txt")

with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Loop through candidates
    for candidate in candidates:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100

        # Determine the winner
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate

        # Write candidate results to the output file
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")