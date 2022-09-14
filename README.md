# An Analysis of Congressional Election Results

## Project Overview
Working with the Colorado board of elections team, the initial task was to complete an election audit of the tabulated results for a U.S. congressional precinct in Colorado. Tasks completed during the election audit included reporting the total number of votes casted, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. 

### Resources
Resources used during this analysis include the following:
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 

### Project Summary
After completing the election audit, the results concluded that a total of 369,711 votes were casted during this election, and there were a total of 3 candidates in the election. A breakdown of the name of each candidate, the total number of votes each candidate received, and the percentage of votes for each candidate is as follows:

- Charles Casper Stockham: received 85,213 total votes and 23.0% of the votes.
- Diana DeGette: received 272,892 total votes and 73.8% of the votes.
- Raymon Anthony Doane: received 11,606 total votes and 3.1% of the votes.

Based on these results, the winner of the election based on popular vote was Diana DeGette, who received 272,892 total votes and 73.8% of the votes.

## Challenge Overview
Taking this analysis one step further, a report of the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout was completed. The overall purpose of this project was to use Python, a popular programming language, to automate the election audit and retrieve the reporting requirements to certify the local congressional election and complete the audit.

### Resources
Resources used during this analysis include the following:
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 

### Challenge Summary
There were 3 counties that participated in the local election - Denver, Jefferson, and Arapahoe. After completing the additional details on county voting requested by the election commission, the results concluded that the total number of votes casted, the voter turnout for each county, and the percentage of votes from each county out of the total count is as follows:

- Total votes casted: 369,711
- Jefferson: 38,855 votes casted and 10.5% of the votes
- Denver: 306,055 votes casted and 82.8% of the votes
- Arapahoe: 24,801 votes casted and 6.7% of the votes 

Based on these results, the county with the largest number of votes was Denver, with 306,055 votes casted and 82.8% of the votes.

Below is an overall summary of the election results that were printed the command line and written on a text file. This text file can also be accessed in the Analysis folder of this repository.

![election_analysis_command](https://user-images.githubusercontent.com/96188669/190229413-09ecedcb-b3ce-4af1-b7c5-e3793f108ee1.png)

Image 1: Election resulted printed on the command terminal


![election_analysis](https://user-images.githubusercontent.com/96188669/190226179-9895c63c-55ee-41da-b12b-e0b5ebaaabc9.png)

Image 2: Election results written to a text file.

### Election Audit Summary
The use cases for data analytics for election auditing are extensive. Beyond local elections, this script can be used to audit nation-wide elections. With minor modifications, this script can be used to audit any election. One of the necessary modifications to the script that would need to be done would be to modify hardcoded values into variables so that future users can specify the values of said variables in relation to their use case. For example, replacing the number value for the index used in the row for loop statement to variable 'i' will allow this for loop statement to be used for a csv, regardless of which row the candidate name is in.  This same idea can be used when assigning variables to lists and dictionaries. Modifying list and dictionary variables within the code to generic variables such as 'i' or 'j' will allow the code to be used in any elections, not just county/local elections.
