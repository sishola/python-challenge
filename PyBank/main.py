# Import dependencies
from statistics import mean
import os
import csv


# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

#Lists to store data read
    amt = []
    mth = []

#read contents of the file
    for row in csvreader:
        amt.append(int(row[1]))
        mth.append(row[0])

total_amt = sum(amt)
num_mths = len(amt)
min_amt = min(amt)
max_amt = max(amt)
avg_amt = mean(amt)


pos_min = amt.index(min(amt))
min_amt_mth = mth[pos_min]

pos_max = amt.index(max(amt))
max_amt_mth = mth[pos_max]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_mths}")
print(f"Total: ${total_amt}")
print(f"Average  Change: ${avg_amt:.2f}")
print(f"Greatest Increase in Profits: {max_amt_mth} (${max_amt})")
print(f"Greatest Decrease in Profits: {min_amt_mth} (${min_amt})")


#Write contents to file
output_file = os.path.join("Output","budget_analysis.txt")

writer = open(output_file,"w")
writer.write("Financial Analysis \n")
writer.write("---------------------------- \n")
writer.write(f"Total Months: {num_mths} \n")
writer.write(f"Total: ${total_amt} \n")
writer.write(f"Average  Change: ${avg_amt:.2f} \n")
writer.write(f"Greatest Increase in Profits: {max_amt_mth} (${max_amt}) \n")
writer.write(f"Greatest Decrease in Profits: {min_amt_mth} (${min_amt}) \n")