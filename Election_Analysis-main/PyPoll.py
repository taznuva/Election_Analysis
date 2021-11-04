# The data we need to retrieve
# 1. The total # of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidates won
# 4. The total # of votes each candidate won
# 5. The winner of the election based on popular vote

#Import the datetime class from the datetime module
import datetime as dt
from os import closerange
#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
#Print the present time
print("The time right now is ", now)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load, "r") as election_data:
    #Read the file object with reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)
 #Print each row in the CSV file
    for row in file_reader:
        print(row)


#Using the open() function with the "w" mode we'll write data to the file.
with open(file_to_save, "w") as txt_file:
    #Write some data in the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


    