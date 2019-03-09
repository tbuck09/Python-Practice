#import modules
import os
import csv
import statistics as stat
import math

#Set file paths
csv_path = os.path.join('Resources','election_data.csv')

with open(csv_path,newline = "") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= ",")

    header= next(csv_reader)
    print(header)

    data_list= [i for i in csv_reader]

    votes= len(data_list)
    print("Total Votes= "+str(votes))

    candidates= [i[2] for i in data_list]
    candidates= set(candidates)
    print(candidates)

#initialize the dictionary for candidates
    cand_dict= {}
    for i in candidates:
        cand_dict[i]= [0,0]
    
#count votes for each candidate
    for i in data_list:
        cand_dict[i[2]][0]= cand_dict[i[2]][0] + 1
    
    for i in cand_dict:
        cand_dict[i][1] = round(cand_dict[i][0]/votes,3) * 100

    print("Election Results")
    print("-"*30)
    print("Total Votes: "+str(votes))
    print("-"*30)
    
    for i in cand_dict:
        print(i+ ": "+ str(cand_dict[i][1])+ "% (" + str(cand_dict[i][0]) + ")")

    print("-"*30)
    
    


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
