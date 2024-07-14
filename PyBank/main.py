import os
import csv

# join path
budget_data = os.path.join("PyBank/Resources/budget_data.csv")

initial_profit= 0
total_change_profits= 0



# open and read csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")


  
    months=[]
    pro_losses=[]
    monthly_change =[]

    for row in csvreader:
        month=row[0]
        pro_loss=row[1]
        months.append(month)
        pro_losses.append(int(pro_loss))
    

print("Financial Analysis")
print("----------------------------")

#calculate total number of months
total_months = len(months)
print("Total Months: "+ str(total_months))


#calculate net total amount of "profit/losses"   
total_pro_losses=sum(pro_losses)
print("Total: "+ "$"+str(total_pro_losses))

for x in range(1, len(pro_losses)):
        monthly_change.append((int(pro_losses[x]) - int(pro_losses[x-1])))

 # calculate average revenue change
monthly_average_change = sum(monthly_change)/(total_months-1)
print("Average_change: "+"$"+str(monthly_average_change))

    # greatest increase in revenue
greatest_increase = max(monthly_change)
greatest_increase_date =months[monthly_change.index(greatest_increase)+1]
print("Greatest Increase in Profits: "+ str(greatest_increase_date)+"  " +"$" + str(greatest_increase))

    #greatest decrease in revenue
greatest_decrease = min(monthly_change)
greatest_decrease_date = months[monthly_change.index(greatest_decrease)+1]
print("Greatest Decrease in Profits: " + str(greatest_decrease_date)+"  " +"$" + str(greatest_decrease))

# open file in write mode,output to output.txt file
file = open("PyBank/analysis/output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("...................................................................................." + "\n")
file.write("total months: " + str(total_months) + "\n")
file.write("Total: " + "$" + str(total_pro_losses) + "\n")
file.write("Average change: " + "$" + str(monthly_average_change) + "\n")
file.write("Greatest Increase in Profits: "+ str(greatest_increase_date)+"  " +"$" + str(greatest_increase)+"\n")
file.write("Greatest Decrease in Profits: " + str(greatest_decrease_date)+"  " +"$" + str(greatest_decrease)+"\n")
file.close()