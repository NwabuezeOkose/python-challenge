#import budget data 
import os
import csv 
#working directory

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               

#This block was made in a for loop to get the number of months in the csv file       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
 #the next few lines are still in the for loop. I used the map and sum instructions to give me the total Revenue (Profit/Losses)
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #To get the average change I used a for loop
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #print(Total)
    
#For Greatest Increase I just created a new variable then used the max function to get the biggest revenue change
#I the made a new variable 'k' so as to get the month where the increase occured
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#For Greatest Decrease the same process as above was used 
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


#print("Total number of months: " + str(len(month)))
print(f"Total number of months: {len(month)}")

#print("Total Revenue (Profit/Losses) over in time period: $ " + str(total_revenue))
print(f"Total revenue (Profit/Losses over in time period: ${total_revenue}")
      
#print("Average monthly change in Revenue : $" + str(monthly_change))
print(f"Average monthly change in revenue: ${monthly_change}")

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
