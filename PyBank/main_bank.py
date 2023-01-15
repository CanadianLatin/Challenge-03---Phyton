
# First we'll import the os module
import os

# Import Module for reading CSV files
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

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

       

print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(date))
print("Total Revenue: $", sum(value))

# in the following for I will use value to get the minimum, maximum, average information
for i in range(1,len(value)):
    difference.append(value[i] - value[i-1])   
    avg_difference = sum(difference)/len(difference)
    max_difference = max(difference)
    min_difference = min(difference)
    max_difference_date = str(date[difference.index(max(difference))])
    min_difference_date = str(date[difference.index(min(difference))])

print("Avereage Revenue Change: $", round(avg_difference))
print("Greatest Increase in Revenue:", max_difference_date,"($", max_difference,")")
print("Greatest Decrease in Revenue:", min_difference_date,"($", min_difference,")")
