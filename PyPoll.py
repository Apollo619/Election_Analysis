# The data we need to retireve. 
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Setting votes to Zero after each candidate.
total_votes = 0 

# Empty list of Candidate names.
candidate_options = []

# Empty dictionary for number of votes for each candidate.
candidate_votes = {}

# Setting empty string variable to declare the winner, winner count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:

        # Increase total vote by 1.
        total_votes += 1

        # Get candidates name
        candidate_name = row[2]

        # Only getting candidate name once each candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Make each candidate a "Key" for the dictionary.
            candidate_votes[candidate_name] = 0
        
        # Increase the candidate vote by 1 each time their name appears. 
        candidate_votes[candidate_name] += 1

# Getting votes from each candidate
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # Calculate the % for each candidate
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candiate name and percentage of vote.
    print(
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning count = votes and winning percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set winning candidate equal to the candidate's name
        winning_candidate = candidate_name

# Print out the winning candidate summary
winning_candidate_summary = (
        f'---------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'---------------------\n')

print(winning_candidate_summary)
