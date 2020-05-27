#import poll
import os
import csv
#working directory
csvpath=os.path.join('..','PyPoll','Resources','election_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    # This line I Declares all variables necessary needed in the program
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

#I used a for loop with the append instruction to get the info for each data of information needed
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #To get the total amount of VOTE COUNT I used the 'len' instruction
    total_votes = (len(votes))
    print(total_votes)

    #To get the votes for each individual candidate I struggled a bit and ended up useing a for Loop 
    #with nested if statements, along with the append anf len instruction to get each of the individual
    #votes for the candidates
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
    
    
    #Again I had trouble with getting the percentages beause it kept on giving results to large decimal
    #places so I used google to find out about the round instruction and was able to get the results needed
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)
    
    #To get the winner I used Basic if and Elif statements
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

        #Print Statements

print(f"Election Results") 
print(f"-----------------------------------") 
print(f"Total Votes: {total_votes}") 
print(f"-----------------------------------") 
print(f"Khan: {khan_percent}% ({khan_votes})") 
print(f"Correy: {correy_percent}% ({correy_votes})") 
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print(f"-----------------------------------") 
print(f"Winner: {winner}") 
print(f"-----------------------------------")