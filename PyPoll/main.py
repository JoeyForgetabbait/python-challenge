#import modules for methods 
import os 
import csv

#import data set 
bankdata = os.path.join("Resources", "election_data.csv")
pybankanalysis = os.path.join("Analysis", "election_analysis.txt")

sumvotes = 0 #total votes cast
candidates = [] #store candidate name
votes_per_candidate = {} #dictionary for storing candidate votes
crnthighestvote = 0
highestvotecandidate = ' ' 



with open(bankdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    #print(csvheader) #make sure data is there
    #print(next(csvreader))

    
     #summarize total votes 
        #extract at candidate name -
        #for candidate in candidate, add to dictionary 
        #add vote count to vpc dictionary
    
    #for i in csvfile: #make sure data is there 
        #print(i)
    for row in csvreader:
        sumvotes += 1 #summarzie votes per candidate
        
        candidate_name = row[2] #look at the candidate name column
        
        if candidate_name not in candidates:
            candidates.append(candidate_name) #if name in list skip over it 
            votes_per_candidate[candidate_name] = 0 #if name is not in list put in the dict. 
        votes_per_candidate[candidate_name] += 1 #if name is in candidate name, add "1" vote to the votes_per_candidate name dictionary
        
with open(pybankanalysis, 'w') as file:
    election_results = (
        'Election Results\n'
        '-------------------------\n'
        f'Total Votes: {sumvotes}\n'
        '-------------------------\n')
    print(election_results)
    file.write(election_results)
    
    
    for name in votes_per_candidate:
        votenum = votes_per_candidate.get(name)
        #print(votenum)
        votepercent = votenum/sumvotes *100 #calculate vote percentageand add it to the vote_per_candidate dictionary
        #print(votepercent)
        candidate_results = (f'{name}: {votepercent:.3f}% ({votenum})\n') #assemble results for file writing/terminal printing
        print(candidate_results)
        file.write(candidate_results)
        
        if votenum > crnthighestvote:
            crnthighestvote = votenum
            highestvotecandidate = name
    
    winning_can = (
            '-------------------------\n'
            f'Winner: {highestvotecandidate}\n'
            '-------------------------')
    print(winning_can)
    file.write(winning_can)

       