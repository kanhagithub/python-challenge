# import poll

import os
import csv

# join path
election_data = os.path.join("Pypoll/Resources/election_data.csv")

# open file in write mode,output to output.txt file
file = open("PyPoll/analysis/output.txt","w")
file.write("Election Results" + "\n")
file.write("-------------------------" + "\n")

# open and read csv

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

#declare variable
    votes = []
    countys = []
    candidates = []
    unique_candidate_list=[]
    Charles_Casper_Stockham=[]
    Diana_DeGette=[]
    Raymon_Anthony_Doane=[]


# read each row of data after header

    for row in csvreader:
        vote=row[0]
        county=row[1]
        candidate=row[2]
        votes.append(int(vote))
        countys.append(county)
        candidates.append(candidate)


# VOTE COUNT
total_votes = (len(votes))
print("Total votes: "+ str(total_votes))
file.write("Total votes: "+ str(total_votes) + "\n")
file.write("-------------------------" + "\n")

#find count of votes by each candidate
out=[[candidates.count(i),i] for i in set(candidates)]
print(out)

#print(type(out))
winner_vote=0

#find votes receiev by candidates and percentage also who got highest vote
for j in out:
    vote=j[0]
    print(j[1] + " : "+  str(round(vote*100/total_votes,3)) +"% ("+ str(vote) +")")
    file.write(j[1] + " : "+  str(round(vote*100/total_votes,3)) +"% ("+ str(vote) +")" + "\n")
    if vote>winner_vote:
        winner_name=j[1]
        winner_vote=vote

#write winner name to file
print("Winner : " + winner_name)
file.write("-------------------------" + "\n")
file.write("Winner : " + winner_name + "\n")
file.write("-------------------------" + "\n")

file.close()