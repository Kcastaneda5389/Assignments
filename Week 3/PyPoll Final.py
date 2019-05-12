#import data file used
import os
import csv

csv_path = 'C:/Users/12104/OneDrive/Data-Bootcamp/03-Python/Instructions/PyPoll/Resources/election_data.csv'

with open (csv_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #list data in file
    
    count = 0
    
    candidatelist = []
    
    unique_candidate = []
    
    vote_count = []
    
    vote_percent = []

#Begin calculating 

    for row in csvreader:

        # Count total number of votes

        count = count + 1

        # Set the candidate names to candidatelist

        candidatelist.append(row[2])


    for x in set(candidatelist):

        unique_candidate.append(x)

        # y is the total number of votes per candidate

        y = candidatelist.count(x)

        vote_count.append(y)

        # z is the percent of total votes per candidate

        z = (y/count)*100

        vote_percent.append(z)

        

    winning_vote_count = max(vote_count)

    winner = unique_candidate[vote_count.index(winning_vote_count)]

    

 

print("--------------------------------------")

print("Election Results")   

print("--------------------------------------")

print("Total Votes :" + str(count))    

print("--------------------------------------")

for i in range(len(unique_candidate)):

            print(unique_candidate[i] + ": " + str(round(vote_percent[i],2)) +"% (" + str(vote_count[i])+ ")")

print("--------------------------------------")

print("The winner is: " + winner)

print("--------------------------------------")



with open('election_results.txt', 'w') as text:

    text.write("Election Results\n")

    text.write("---------------------------------------\n")

    text.write("Total Vote: " + str(count) + "\n")

    text.write("---------------------------------------\n")

    for i in range(len(set(unique_candidate))):

        text.write(unique_candidate[i] + ": " + str(round(vote_percent[i],2)) +"% (" + str(vote_count[i]) + ")\n")

    text.write("---------------------------------------\n")

    text.write("The winner is: " + winner + "\n")

    text.write("---------------------------------------\n")