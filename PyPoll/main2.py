import os
import csv
total_votes = 0
Candidate_List = []
vote_List = []
Candidate_Index = 0
counter = 0
highest = 0 

election_data = 'Resources/election_data.csv'

with open(election_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        total_votes +=  1

        try:
            Candidate_Index = Candidate_List.index(row[2])
        except ValueError:
            Candidate_List.append(row[2])
            vote_List.append(0)
            Candidate_Index = len(Candidate_List) -1
        vote_List[Candidate_Index] +=1

output_path = 'Resources/election_result.txt'
with open(output_path, 'w') as txt_file:
    print("Election Results", file = txt_file)
    print("-"*10, file = txt_file)
    print(f"Total Votes: {total_votes}", file = txt_file)
    print("-"*10, file = txt_file)
    for candidate in Candidate_List:
        print(f"{candidate}: {(vote_List[counter]/total_votes)*100} % ({vote_List[counter]})",file = txt_file)
        if vote_List[counter] > highest:
            highest = vote_List[counter]
            winner = candidate
        counter += 1
    print("-"*10, file = txt_file)
    print (f"Winner:{winner}", file = txt_file)
    print("-"*10, file = txt_file)

counter = 0
highest = 0
winner = ""

print("Election Results")
print("-"*10)
print(f"Total Votes: {total_votes}")
print("-"*10)
for candidate in Candidate_List:
    print(f"{candidate}: {(vote_List[counter]/total_votes)*100} % ({vote_List[counter]})")
    if vote_List[counter] > highest:
        highest = vote_List[counter]
        winner = candidate
    counter += 1
print("-"*10)
print (f"Winner:{winner}")
print("-"*10)

