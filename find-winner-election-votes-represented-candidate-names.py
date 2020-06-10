'''
Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate. 
Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.
https://www.geeksforgeeks.org/find-winner-election-votes-represented-candidate-names/
'''



votes = ["john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]
Election_count={}
for i in votes:
    Election_count[i]=Election_count.get(i,0)+1
print(Election_count)
Election_result=sorted(Election_count,key=lambda x:(x[1],len(x[0])),reverse=True)
print(Election_result)
