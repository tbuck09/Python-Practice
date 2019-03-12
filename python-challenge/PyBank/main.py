#import modules
import os
import csv
import statistics as stat
import math

#Set file paths
csv_path = os.path.join('Resources','budget_data.csv')

#Open the .csv
with open(csv_path,newline = "") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= ",")

#Store the header in a variable and move onto the first row of data (next())
#If this is excluded, the first row will still need to be worked around
#or the header will cause a ValueError due to the string
    header= next(csv_reader)

    data_list= [row for row in csv_reader]

    prof_loss= [int(i[1]) for i in data_list]
    max_prof= [prof_loss.index(max(prof_loss)),max(prof_loss)]
    max_loss= [prof_loss.index(min(prof_loss)),min(prof_loss)]
    change_prof_loss= [prof_loss[i+1] - prof_loss[i] for i in range(0,len(prof_loss)-1)]

    print("Financial Analysis")
    print("-"*20)
    print("Total Months: "+str(len(data_list))+" rows")
    print("Total: $"+ str(sum(prof_loss)))
    print("Average change: $"+str(round(stat.mean(change_prof_loss),2)))
    print("Greatest increase in profit: "+data_list[max_prof[0]][0]+" ($"+str(max_prof[1])+")")
    print("Greatest decrease in loss: "+data_list[max_loss[0]][0]+" ($"+str(max_loss[1])+")")

#Write to text file
fin_analysis= open("Financial_Analysis.txt","w")

fin_analysis.write("Financial Analysis\n")
fin_analysis.write("-"*20+'\n')
fin_analysis.write("Total Months: "+str(len(data_list))+"\n")
fin_analysis.write("Total: $"+ str(sum(prof_loss))+"\n")
fin_analysis.write("Average change: $"+str(round(stat.mean(change_prof_loss),2))+"\n")
fin_analysis.write("Greatest increase in profit: "+data_list[max_prof[0]][0]+" ($"+str(max_prof[1])+")\n")
fin_analysis.write("Greatest decrease in loss: "+data_list[max_loss[0]][0]+" ($"+str(max_loss[1])+")\n")

fin_analysis.close()