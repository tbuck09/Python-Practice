#Import modules
import os
import csv

#Set file paths
csv_path = os.path.join('Resources','election_data.csv')

#Open file
with open(csv_path,newline = "") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= ",")
#Assign header row and move past it
    header= next(csv_reader)
#Convert from text object to list for aggregation and iteration
    data_list= [i for i in csv_reader]
#Count votes
    votes= len(data_list)
#Pick out unique candidate names
    candidates= set([row[2] for row in data_list])
#Initialize list of Candidate name, Total votes, and Percent of votes for each candidate
    cand_list= [[i,0,0] for i in candidates]
#Count votes for each candidate 
    for row in data_list:
        for cand in cand_list:
            if row[2] == cand[0]:
                cand[1] = cand[1] + 1
#Calculate percent of votes for each candidate
    for cand in cand_list:
        cand[2] = round(cand[1]/votes,3)
#Sort the candidates by most to least votes
    cand_list.sort(key= lambda x: x[2],reverse= True)

#Print the Election Results
    print("Election Results")
    print("-"*30)
    print("Total Votes: "+str(votes))
    print("-"*30)
#Print each candidate, the percent of votes, and the total votes for each candidate
    for cand in cand_list:
        print(cand[0]+ ": "+ '%.f' % (cand[2]*100) + "% (" + str(cand[1]) + ")")
    print("-"*30)
#Print the winner
    print("** " + cand_list[0][0].upper() + " WINS!" + " **")
    print("-"*30)

#Write to text file
elec_results= open("Election_Results.txt","w")

elec_results.write("Election Results\n")
elec_results.write("-"*30+"\n")
elec_results.write("Total Votes: "+str(votes)+"\n")
elec_results.write("-"*30+"\n")
#Print each candidate, the percent of votes, and the total votes for each candidate
for cand in cand_list:
    elec_results.write(cand[0]+ ": "+ '%.f' % (cand[2]*100) + "% (" + str(cand[1]) + ")"+"\n")
elec_results.write("-"*30+"\n")
#Print the winner
elec_results.write("** " + cand_list[0][0].upper() + " WINS!" + " **"+"\n")
elec_results.write("-"*30+"\n")

elec_results.close()