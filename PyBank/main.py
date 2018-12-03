import os                                                               #Import libraries to work with Python OS and CSV
import csv
month_counter = 0
PL_counter = 0
average_change = 0
data = []

budget_data_csv_path = os.path.join("..", "Resources", "budget_data.csv")
csv_out_path = os.path.join("..","Resources","Output","PyBank_output.csv")   #This is to tell the program that the CSV file is on this path (different to where .py is)

with open(budget_data_csv_path, newline="") as csvfile:                      #Open the CSV file and every "" we have a new line of the doc
    csv_reader = csv.reader(csvfile, delimiter=",")                     #Read the CSV document with the characteristic that is delimited by ","

    csv_header = next(csvfile)                                        # Read the header row first (skip this part if there is no header)
    # print(f"Header: {csv_header}")                                    # Print the header of the first row
                                                                        # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file
    for row in csv_reader:                                              # Read through each row of data after the header                                        # Convert row to float and compare to grams of fiber
             # print(f'{row[0]}                       {row[1]}')
             month_counter += 1
             PL_counter = PL_counter + int(row[1])
             data.append(row)

i=0
acumulator_avg = 0.00
contador_avg_2 = 0.00
avg = 0.00
detect_inc = []
pre_average_change = 0
menor_pre_average_change = 0 
counter = 0
array_average = [0,1]
menor_array_average = [3,4]

while i < month_counter-1:
    average_change = int(data[i+1][1])-int(data[i][1])
    acumulator_avg += average_change

    if average_change > pre_average_change:
        pre_average_change = average_change
        array_average[0]=data[i+1]
        array_average[1]=average_change
    if average_change < menor_pre_average_change:
        menor_pre_average_change = average_change
        menor_array_average[0]=data[i+1]
        menor_array_average[1]=average_change

    i += 1

avg = acumulator_avg/(month_counter-1)

print("Financial Analysis") 
print("---------------------------------------")   
print(f'Total Months: {month_counter}')
print(f'Total: ${PL_counter}')
print(f'Average  Change: ${avg}')
print(f'Greatest Increase in Profits: {array_average[0][0]} ${array_average[1]}')
print(f'Greatest Decrease in Profits: {menor_array_average[0][0]} ${menor_array_average[1]}')


f = open(csv_out_path,'w')

f.write(f'Financial Analysis\n---------------------------------------\nTotal Months: {month_counter}\nTotal: ${PL_counter}\nAverage  Change: ${avg}\nGreatest Increase in Profits: {array_average[0][0]} ${array_average[1]}\nGreatest Decrease in Profits: {menor_array_average[0][0]} ${menor_array_average[1]}')

f.close()