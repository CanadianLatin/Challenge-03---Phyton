
# First we'll import the os module
import os

# Import Module for reading CSV files
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")
textpath = os.path.join(".","Analysis","results.txt")

# Lists to store the Data
date = []
value = []
difference = []



# in this loop I added column 1 and 2 date and value. in that way I can operate them and print them at the end.

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # Add date
        date.append(row[0])

        #Add Profit/Losses
        value.append(int(row[1]))

       

print('\n'+'\n'+'\n'+'\t'+'\t'+"Financial Analysis:")
print( '\n'+"-----------------------------------------------------")
print('\n'+"Total Months:"+'\t'+'\t'+'\t', len(date))
print('\n'+"Total:"+'\t'+'\t'+'\t'+'\t'+"$ ", sum(value))

# in the following for I will use value to get the minimum, maximum, average information
for i in range(1,len(value)):
    difference.append(value[i] - value[i-1])   
    avg_difference = sum(difference)/len(difference)
    max_difference = max(difference)
    min_difference = min(difference)
    max_difference_date = str(date[difference.index(max(difference))+1])
    min_difference_date = str(date[difference.index(min(difference))+1])

print('\n'+"Average Change:"+'\t'+'\t'+'\t'+"$ ", round(avg_difference,2))
print('\n'+"Greatest Increase in Profits: "+'\t', max_difference_date,"($", max_difference,")")
print('\n'+"Greatest Decrease in Profits: ", min_difference_date,"($", min_difference,")"+'\n'+'\n'+'\n')


with open(textpath, 'w') as f:
    f.write('\n'+'\n'+'\n'+'\t'+'\t'+"Financial Analysis:")
    f.write( '\n'+"-----------------------------------------------------")
    f.write('\n'+"Total Months:"+'\t'+'\t'+'\t'+str (len(date)))
    f.write('\n'+"Total:"+'\t'+'\t'+'\t'+'\t'+"$ "+str(sum(value)))
    f.write('\n'+"Average Change:"+'\t'+'\t'+'\t'+"$ "+ str(round(avg_difference,2)))
    f.write('\n'+"Greatest Increase in Profits: "+'\t'+ str(max_difference_date)+'\t'+"($"+str(max_difference)+")")
    f.write('\n'+"Greatest Decrease in Profits: "+'\t'+ str( min_difference_date)+'\t'+"($"+str(min_difference)+")")

    