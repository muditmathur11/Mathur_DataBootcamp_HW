#Mudit Mathur
#06/29/19
#PyPoll

import csv
import os

#outputting results to a text file called Poll results
output_file = "Mathur_Poll_Results.txt"
#open the output file
file = open(output_file, 'w')

candidates = []
all_votes = []

def printResults():
    winner_count = 0
    total_votes = len(rowsArray) - 1
    winners_output = ''
    
    print('Election Results')
    print('----------------------------')
    print('Total Votes: ', total_votes)
    print('----------------------------')

    for can in candidates:
        candidate_count = all_votes.count(can)
        percentage_vote =  round((candidate_count / total_votes) * 100, 3)
        winners_output = winners_output + can + ': ' + str( percentage_vote) + '% (' + str(candidate_count) + ')' + '\n'
        print(can + ': ' + str( percentage_vote) + '% (' + str(candidate_count) + ')')

        if candidate_count > winner_count:
            winner_count = candidate_count
            winner = can

    print('----------------------------')
    print('Winner : ' + winner)
    print('----------------------------')

    file.write('Election Results\n')
    file.write('----------------------------\n')
    file.write("Total Votes: " + str(total_votes) + '\n')
    file.write('----------------------------\n')
    file.write(winners_output)
    file.write('----------------------------\n')
    file.write('Winner : ' + winner + '\n')
    file.write('----------------------------\n')

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:

    # create CSV reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # converts csvreader to list
    rowsArray = list(csvreader)

    # Print the contents of each row
    for i in range(1, len(rowsArray)):
        # if candidate no in candidates array
        if rowsArray[i][2] not in candidates:
            # add candidate to candidates array
            candidates.append(rowsArray[i][2])

        # add each candidate to all_votes array
        all_votes.append(rowsArray[i][2])

printResults()