## Using f strings in python

## Old code (no f strings involved)
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes/total_votes) * 100
print("I received " +str(percentage_votes)+"% of the total votes")

## New code with f strings involved
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes/total_votes*100}% of the total votes.")

## F Strings in Dictionaries
counties_dict = {"Arapahoe":369237,"Denver":413229,"Jefferson":390222}

## Old code (no f strings involved)
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

## New code with f strings involved
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

## Multi-line F Strings - can use this to print multiple strings or lines to the screen. i.e.:
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

## Format Floating Point Decimals
    ## General Format
        ## f'{value:{width}.{precision}}'
    ## width = the number of characters used to display the value
    ## precision = indicates the number of decimal places to format the value (i.e use .2f to indicate formatting to 2 decimal pts)
    
    ## can use a thousands sep with a comma:
        ## f'{value:{width},.{precision}}'