import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
elec_data = os.path.join('Resources', 'election_data.csv')

#Candidate List
#Vote List 
#Percetage Total List
    #lists
CN = []
CV= []
PV = []


# A counter for the total number
TV = 0

with open(elec_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        TV = TV + 1 

        if row[2] not in CN:
            CN.append(row[2])
            placeholder = CN.index(row[2])
            CV.append(1)
        else:
        #else row[2] not in candidates:
            placeholder = CN.index(row[2])
            CV[placeholder] = CV[placeholder] + 1
    
    #  The percentage of votes each candidate won
    for votes in CV:
        percentage = "%.3f%%" %(round((votes/TV) * 100))
        PV.append(percentage)
    
    # The winner of the election
    W = max(CV)
    placeholder = CV.index(W)
    WC = CN[placeholder]

# Test print for txt file
print("'''text")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(TV)}")
print("--------------------------")
for i in range(len(CN)):
    print(f"{CN[i]}: {str(PV[i])} ({str(CV[i])})")
print("--------------------------")
print(f"Winner: {WC}")
print("--------------------------")
print("'''")

# Print to txt
output = open("PyPollOutput.txt", "w")
l1 = "'''text"
l2 = "Election Results"
l3 = "--------------------------"
l4 = str(f"Total Votes: {str(TV)}")
l5 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n{}\n'.format(l1, l2, l3, l4,l5))
for x in range(len(CN)):
    line = str(f"{CN[x]}: {str(PV[x])} ({str(CV[x])})")
    output.write('{}\n'.format(line))
l6 = "--------------------------"
l7 = str(f"Winner: {WC}")
l8 = "--------------------------"
l9 = "'''"
output.write('{}\n{}\n{}\n{}\n'.format(l6, l7, l8,l9))
