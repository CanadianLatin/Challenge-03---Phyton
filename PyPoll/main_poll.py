
# First we'll import the os module
import os

# Import Module for reading CSV files
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")
textpath = os.path.join(".","Analysis","results.txt")

# Lists to store the Data
id = []
county = []
candidate = []
candidate_votes = {}


#we are going to store the unique 
unique = []



# in this loop I added column 1 and 2 date and value. in that way I can operate them and print them at the end.

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # Add Ballot ID
        id.append(int(row[0]))

        #Add County
        county.append(row[1])

        #Add Candidate
        name=row[2]
        candidate.append(name)
        if name not in unique:
            unique.append(name)
            candidate_votes[name]= 1
        else :
            candidate_votes [name] += 1
            

        

total_votes=len(id)      

print('\n'+'\n'+'\n'+'\t'+'\t'+"Election Results:")
print( '\n'+"-----------------------------------------------------")
print('\n'+"Total Votes:"+'\t'+'\t'+ str(total_votes) )
print( '\n'+"-----------------------------------------------------"+"\n\n")



# Have a index of the unique candidates
# print(set(candidate))

""" for k,v in candidate_votes.items():
    print(k,str(format ((int(v)/total_votes),".3%"))," (",v,")")
    print('\n') """


# list out keys and values separately for the dictionary that contains the candidates and votes
key_list = list(candidate_votes.keys())
val_list = list(candidate_votes.values())

#finding the maximum number of votes
max_votes = max(val_list)

#index of the max votes (what position are they in)
index_votes=list(candidate_votes.values()).index(max_votes)

#winner is: having the index get the key name
winner = key_list[index_votes]


#the following loop prints the dictionary keys (candidates) and the votes (values). I have to write on the external 
#file inside of the loop

with open(textpath, 'w') as f:
    f.write('\n'+'\n'+'\n'+'\t'+'\t'+"Election Results:")
    f.write( '\n'+"-----------------------------------------------------")
    f.write('\n'+"Total Votes:"+'\t'+'\t'+ str(total_votes))
    f.write( '\n'+"-----------------------------------------------------"+"\n\n")
    for k,v in candidate_votes.items():
        print(k,str(format ((int(v)/total_votes),".3%"))," (",v,")",'\n')
        print('\n')
        f.write(str(k)+"  "+str(format ((int(v)/total_votes),".3%"))+" ("+str(v)+")")
        f.write('\n')
    f.write( '\n'+"-----------------------------------------------------")
    f.write('\n'+"Winner:"+'\t'+'\t'+'\t'+ winner)
    f.write( '\n'+"-----------------------------------------------------"+'\n')




# print the winner in the screen
print( '\n'+"-----------------------------------------------------")
print('\n'+"Winner:"+'\t'+'\t'+'\t'+ winner)
print( '\n'+"-----------------------------------------------------"+'\n')
 