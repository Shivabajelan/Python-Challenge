# import modules to create file path and reading CSV file
import os
import csv

# set path for file
budget_data = os.path.join("Resources", "budget_data.csv")

# initialise variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0

# create lists for dates and profit/loss changes
dates = []
profit_loss_changes = []


# open the csv file 
with open(budget_data) as csvfile:

     # read csv file it using the reader function
     csvreader = csv.reader(csvfile, delimiter=',')

     # skip the header row first
     header = next(csvreader) 

     # read each row of data after the header
     for row in csvreader:
        
        # extract data from the current row
        date = row[0]
        profit_loss = int(row[1])
        
        # calulate the total number of months
        total_months += 1
        
        # calculate net total amount of "Profit/Losses" over the entire period
        total_profit_losses += profit_loss

     # calculate the change in "Profit/Losses" over the entire period and appending to our lists
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            dates.append(date)
            profit_loss_changes.append(change)

        

            # calculate the average change in profit/lost over the entire period
            average_change = sum(profit_loss_changes) / len(dates)

            # calculate the greatest increase in profits (date and amount) over the entire period
            greatest_increase_profit = max(profit_loss_changes)
            greatest_increase_date = dates[profit_loss_changes.index(greatest_increase_profit)]

            # calculate the greatest decrease in profits (date and amount) over the entire period
            greatest_decrease_profit = min(profit_loss_changes)
            greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease_profit)]
        # update the previous_profit_loss for the next row
        previous_profit_loss = profit_loss
# print the clculated results
print("Financial Analysis")
print('.............................')
print(f"Total Months: {total_months}")      
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} ,  (${greatest_increase_profit})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ,  (${greatest_decrease_profit})")


with open("budgetfile.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write('.............................\n')
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_losses}\n")
    textfile.write(f"Average Change: ${round(average_change,2)}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} ,  (${greatest_increase_profit})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ,  (${greatest_decrease_profit})\n")