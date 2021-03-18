# The data we need to retireve. 
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row. 
    headers = next(file_reader)
    print(headers)
                


# A complete list of candidates who received votes
# The percentage of votes ech candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
##with open(file_to_save, "w") as txt_file:
    # Write some data to the file. 
    ##txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")


