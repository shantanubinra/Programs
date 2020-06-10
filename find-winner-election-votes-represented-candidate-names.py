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
