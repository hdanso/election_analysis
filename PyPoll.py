## The data we need to retrieve:
    ## 1. The total number of votes casted
    ## 2. A complete list of candidates who received votes
    ## 3. The percentage of votes each candidate won
    ## 4. The total number of votes each candidate won
    ## 5. The winner of the election based on popular 

## Import os and csv modules (Adding our dependencies)
import os
import csv

## Assign a variable to load a file from an indirect path
file_to_load = os.path.join("Resources","election_results.csv")

## Assign a variable to save the file to an indirect path
file_to_save = os.path.join("analysis","election_analysis.txt")

## Initialize a total vote counter (accumulator) - set to zero and place before opening a file to return variable to 0 each time we run the file
total_votes = 0

## Declare a new list for Candidate options
candidate_options = []

## Declare a new dictionary for candidate votes
candidate_votes = {}

## Open the election results and read the file
with open(file_to_load) as election_data:

    ## Read the file object with the reader function
    file_reader = csv.reader(election_data)

    ## Read the header row
    headers = next(file_reader)

    ## Print each row in the CSV File
    for row in file_reader:
        ## Increment the total votes variable by 1 to add to the total vote count (this was shortened from total_votes = total_votes + 1)
        total_votes += 1
        
        ## Print the candidate name from each row
        candidate_name = row[2]

 
        ## Add the candidate name to the candidate_options list if the candidate doesn't match any exisiting candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            ## Create each candidate as a key and begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        ## Increment candidate vote by 1 each time we move through a row (needs to be in for loop but outside of if statement)
        candidate_votes[candidate_name] += 1

        ## Iterate through the candidate options list
        for candidate_name in candidate_votes:

            ## Get the vote count of a candidate from the candidate_votes dictionary
            votes = candidate_votes[candidate_name]

            ## Calculate the percentage of votes
            vote_percentage = float(votes)/float(total_votes) * 100

            ## Print the candidate name and percentage of votes
            print(f"{candidate_name}: received {vote_percentage}% of the vote.")

## Print the total votes
print(total_votes)

## Print the candidate list
print(candidate_options)

## Print the candidate vote dictionary
print(candidate_votes)



## Open the file to save as a txt file
with open(file_to_save, "w") as txt_file:

    ## Write three counties to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
