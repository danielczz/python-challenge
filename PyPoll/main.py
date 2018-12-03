import os                               #Import libraries to work with Python OS and CSV
import csv
import pandas as pd

votes_counter = 0                       #Declaration of variables. 
PL_counter = 0
average_change = 0
data = []
array_votes = []

election_data_csv_path = os.path.join("..", "Resources", "election_data.csv")  
csv_out_path = os.path.join("..","Resources","Output","PyPoll_output.csv")      #This is to tell the program that the CSV file is on this path (different to where .py is)

with open(election_data_csv_path, newline="") as csvfile:                       #Open the CSV file and every "" we have a new line of the doc
    csv_reader = csv.reader(csvfile, delimiter=",")                             #Read the CSV document with the characteristic that is delimited by ","

    csv_header = next(csvfile)                                                  # Read the header row first (skip this part if there is no header)
    # print(f"Header: {csv_header}")                                              # Print the header of the first row
#                                                                               # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file
    for row in csv_reader:                                                      # Read through each row of data after the header                                        # Convert row to float and compare to grams of fiber
        # print(f'{row[0]}      {row[1]}       {row[2]}')
        votes_counter += 1
#              PL_counter = PL_counter + int(row[1])
        data.append(row)

i=0                                     #Declaration of variables.
j=0
contador=0
contador_1=0
contador_2=0
contador_3=0
array_candidates = []

while i < votes_counter - 1:                                                    #Lets create an array of candidates. 
    if data[i+1][2] != data[i][2] and data[i+1][2] not in array_candidates:
        array_candidates.append(data[i+1][2])
    i += 1

while j < votes_counter - 1:                                                    #Lets count the votes for each candidate. 
    if data[j][2] == array_candidates[0]: 
            contador += 1
    if data[j][2] == array_candidates[1]: 
            contador_1 += 1
    if data[j][2] == array_candidates[2]: 
            contador_2 += 1
    if data[j][2] == array_candidates[-1]: 
            contador_3 += 1
    j += 1

# for candidate in array_candidates:
#      print(candidate)

calc_porc = round(contador/votes_counter*100, 4)                                #Lets calculate the percentage of votes for each candidate.                                    
calc_porc_1 = round(contador_1/votes_counter*100, 4)
calc_porc_2 = round(contador_2/votes_counter*100, 4)
calc_porc_3 = round(contador_3/votes_counter*100, 4)
winner = max(contador,contador_1,contador_2,contador_3)

if winner == contador:                                                          #Lets calculate the winner.                                                  
    winner_name = array_candidates[0]
elif winner == contador_1:
    winner_name = array_candidates[1]
elif winner == contador_2:
    winner_name = array_candidates[2]
elif winner == contador_3: 
    winner_name = array_candidates[3]

print("Election results")                                                       #Print results. 
print("---------------------------------------")   
print(f'Total Votes: {votes_counter}')
print("---------------------------------------")   
print(f'Khan: {calc_porc_1}% ({contador_1})')
print(f'Correy: {calc_porc}% ({contador})')
print(f'Li: {calc_porc_2}% ({contador_2})')
print(f'O"Tooley: {calc_porc_3}% ({contador_3})')
print("---------------------------------------")
print(f'Winner: {winner_name}')
print("---------------------------------------")


f = open(csv_out_path,'w')                                                      #Output file. 

f.write(f'Election results\n---------------------------------------\n\
Total Votes: {votes_counter}\n---------------------------------------\n\
Khan: {calc_porc_1}% ({contador_1})\n\
Correy: {calc_porc}% ({contador})\n\
Li: {calc_porc_2}% ({contador_2})\n\
O"Tooley: {calc_porc_3}% ({contador_3})\n\
---------------------------------------\n\
Winner: {winner_name}\n---------------------------------------')

f.close()

