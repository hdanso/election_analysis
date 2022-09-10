## ITERATING THROUGH LISTS AND TUPLES 

## Example of conditional (while) loops
x = 0
while x <= 5:
    print(x)
    x = x + 1

## Example of count (for) loops
counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)

## Example of count (for) loop using the range function = range() creates an iterable object or list
for num in range(5):
    print(num)

## Example of for loop using indexing and the range() function
    ## variable i used to indicate the index (or position 0, 1, 2 in the list)
    ## use len() function to get the length of the list as an integer
for i in range(len(counties)):
    print(counties[i])

## ITERATING THROUGH DICTIONARIES
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

## Example of getting keys of a dictionary using a for loop
for county in counties_dict:
    print(county)

    ## you can also use the keys() function to iterate over a dictionary to get the keys (will print each key in order)
    for county in counties_dict.keys():
        print(county)

## Example of getting values of a dictionary using the values() function and for loop (will print each value in order)
for voters in counties_dict.values():
    print(voters)

    ## you can also use the format dictionary_name[key] to get the value of keys
    for county in counties_dict:
        print(counties_dict[county])
    ## or use get() function to get the value of keys
    for county in counties_dict:
        print(counties_dict.get(county))

## Example of getting keys and values of a dictionary using items() function - NOTE: 1st variable declared is assigned to keys and 2nd variable assigned to values 
    for county, voters in counties_dict.items():
        print(county,voters)

## ITERATE THROUGH A LIST OF DICTIONARIES

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

## Example of using for loop to get each dictionary in a list of dictionaries
for county_dict in voting_data:
    print(county_dict)

## Example of using range() in for loop to get each dictionary key in a list of dictionaries 
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

## Example of using nested for loop to retrieve the values from each dictionary in a list of dictionaries
for county_dict in voting_data: ## this will retrieve each dictionary
    for value in county_dict.values(): ## first set up value variable and use value() function to with county_dict variable to get each value
        print(value)

## Example of getting only 1 value from a dictionary in a list of dictionaries
for county_dict in voting_data:
    print(county_dict['county'])