"Esto es una prueba".

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
             # print(f'{row[0]}		                  {row[1]}')
             month_counter += 1
             PL_counter = PL_counter + int(row[1])
             data.append(row)
