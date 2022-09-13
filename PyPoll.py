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

## Declare variable for empty string value for the winning candidate
winning_candidate = ""

## Declare a winning count variable and equal to 0
winning_count = 0

## Declare a winning percentage variable and equal to 0
winning_percentage = 0

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

## Save the results to text file
with open(file_to_save, "w") as txt_file:

    ## Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    ## Save the final vote count to the text file
    txt_file.write(election_results)
    

    ## Iterate through the candidate options list
    for candidate_name in candidate_votes:

        ## Get the vote count of a candidate from the candidate_votes dictionary
        votes = candidate_votes[candidate_name]

        ## Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        ## Print the candidate name, vote count and percentage of votes to the terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        ## Print each candidate's voter count and percentage to the terminal
        print(candidate_results)

        ## Save the candidate results to our text file
        txt_file.write(candidate_results)

    ## Determine winning vote count and candidate

    ## Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            ## If true, set winning count to vote count value
            winning_count = votes

            ## If true, set winning percentage to vote percentage
            winning_percentage = vote_percentage
            
            ## If true, set winning candidate to candidate name key
            winning_candidate = candidate_name

    ## Print the winning candidate, vote count, and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    ## Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


