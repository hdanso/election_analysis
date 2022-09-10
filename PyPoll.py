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

## Open the election results and read the file
with open(file_to_load) as election_data:

    ## To do: read and analyze the data

    ## Read the file object with the reader function
    file_reader = csv.reader(election_data)

    ## Print each header row in the CSV file
    headers = next(file_reader)
    print(headers)

## Open the file to save as a txt file
with open(file_to_save, "w") as txt_file:

    ## Write three counties to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
