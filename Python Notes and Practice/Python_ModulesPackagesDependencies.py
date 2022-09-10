## Dependencies - modules and packages that allow you to increase functional programming of your code, or speed, and efficiency
## Packages - folders that contain a set of Python modules. Use import statement to import packages
## Modules - python files with a .py extension that has functions, classes or variables defined and implemented
    ## To use a specific function, class, or variable from a module, you use a statement like from import.

## Using datetime module to get today's date using VS Code

## Import the datetime class from the datetime 
import datetime

## Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()

## Print the present time
print("The time right now is ", now)

## Use an abbreviated alias to avoid confusion importing module vs class
import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)

## The CSV Module

## CSV Module imported by using the statement import and then the module name (csv)

## View the functions available in the csv module:
import csv
dir(csv)

## dir() can take a python module, a variable (i.e. a dictionary - will return all the functions avaialble on the variable) or a data type (i.e. a string - will return all the attributes and methods that can be used with the data type)

