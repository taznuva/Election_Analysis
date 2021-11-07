# Election_Analysis

## Overview of Election Audit
### Purpose 
    
    The purpose of this challenge serves as an introduction to Python by getting familiar with the coding syntax, using 'for' loops, and conditionals to help Seth and Tom with the election audit. A fun, simple, and easy to understand code to help the election committee gather the data they need for the current election and for future elections. 


## Election-Audit Results:

  - There were a total of 369,711 votes cast in this congressional election.
  - There were 3 counties that voted in this election:
     - Jefferson: 38,855 votes (10.5%)
     - Denver: 306,055 votes (82.8%)                                      
     - Arapahoe: 24,801 votes (6.7%)                                  
  - Denver had the most votes with 82.8% of total votes in this election.
  - There were 3 candidates who ran for this election:
     - Charles Casper Stockham: 85,213 votes (23.0%)
     - Diana DeGette: 272,892 votes (73.8%)
     - Raymon Anthony Doane: 11,606 votes (3.1%)
  - Diana DeGette won the election with a whopping 272,892 votes! That's 73.8% out of the total votes!
<img width="267" alt="Screen Shot 2021-11-07 at 4 13 55 PM" src="https://user-images.githubusercontent.com/33046642/140662072-075767c8-5315-447c-a6c2-38de9ae9cb55.png">

## Election-Audit Summary:
The election commission can use this script for any elections both current and in future with little to no modifications needed. One foreseeble problem happening can be the format of the election results csv file. If the index of the rows do not match, one simply has to change the index number in the code. For example, the original format of the election results csv file looks like below. In the script we reference to the row index for county and candidate name. 

<img width="343" alt="Screen Shot 2021-11-07 at 4 23 07 PM" src="https://user-images.githubusercontent.com/33046642/140662322-fcb77212-4693-4424-a8b2-cab1d16a8f11.png"><img width="339" alt="Screen Shot 2021-11-07 at 4 25 34 PM" src="https://user-images.githubusercontent.com/33046642/140662414-15c20618-91ec-4e47-a140-4d7bac275938.png">

If the format of the row index on the election results changed, such as county name was at Index[0], candidate name became Index[1], and Ballot ID at Index[2], etc. one would just have to change the index number in the script to correlate to the correct one in the csv file. 

In addition, another modification that may be needed is when you load a file to the path. The election results will not be the same for each election and maybe saved under different names. One simple modification is to replace the name of the text file that's set for the file_to_load variable. Starting from the file path code, let's say instead of 'election_results.csv', this new file is called 'Election_2018_results.csv'. The code would look like the below.

 Before:
 
<img width="477" alt="Screen Shot 2021-11-07 at 4 41 13 PM" src="https://user-images.githubusercontent.com/33046642/140662854-b804acd5-b470-4d7f-b6ec-b666ed2a38a5.png">

After:

<img width="513" alt="Screen Shot 2021-11-07 at 4 42 02 PM" src="https://user-images.githubusercontent.com/33046642/140662879-407c19af-cbb4-4c14-9e2e-931ad609f835.png">

The same process goes for the file_to_save code as well if you wanted to output to a different text file than the one previously used. 

If this was a nationwide election, such as the Presidential Elections, we would be using States instead of Counties. A simple modification for that would just to replace the variable names: county_name/county_list/county_votes to state_name/state_list/state_votes respectively throughout the script as well as in the f-string statements outputting the results. 



