# import modules to create file path and reading CSV file
import os
import csv

# set path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")
    
# initialize variables 
total_votes = 0
candidate_list = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0  

print("Election Results")
print("-------------------------------------")

# read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # iterate through each row in the dataset to extract candidate
    for row in csvreader:
        total_votes= total_votes + 1
        candidate=row[2]
            
         # check if the candidate is already in the dictionary or not
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate]= candidate_votes[candidate] + 1

    print(f"Total Votes: {total_votes}")
    print("-------------------------------------")

with open("electionfile.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")

    # calculate each candidate votes
    for candidate_winner in candidate_votes:
        votes=candidate_votes.get(candidate_winner)
        # vote_percentage= 0
        vote_percentage=float(votes)/float(total_votes)*100

        # find the winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate_winner 
        final_list = f"{candidate_winner}: {vote_percentage:.3}% ({votes})\n"
        print(final_list,end="")

        textfile.write(final_list)
        
    print("-------------------------------------")
    print(f'Winner: {winning_candidate}')
    print("-------------------------------------")
    
    # writet the rest of analysis to the textfile
    textfile.write("-------------------------\n")
    textfile.write(f'Winner: {winning_candidate}\n')
    textfile.write("-------------------------------------")

    
   
    
 





    