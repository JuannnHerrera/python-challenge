### Main Script to run each analysis
import os
import csv

# Set the file path
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
net_total = 0
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = []
# The greatest increase in profits (date and amount) over the entire period
greatest_increase = {"date": "", "amount": 0}
# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = {"date": "", "amount": 0}

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_total += profit_loss

        if total_months > 1:
            change = profit_loss - prev_profit_loss
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        prev_profit_loss = profit_loss

average_change = round(sum(changes) / len(changes), 2)

# Generate and write output_budget_data.txt
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

output_path = os.path.join("PyBank", "analysis", "output_budget_data.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
