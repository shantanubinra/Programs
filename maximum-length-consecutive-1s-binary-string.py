'''
We are given a binary string containing 1’s and 0’s. Find maximum length of consecutive 1’s in it.
https://www.geeksforgeeks.org/maximum-length-consecutive-1s-binary-string-python-using-map-function/
'''
binary_s='11000111111111111'
binary_splitter=binary_s.split('0')
#print(binary_splitter)
length=0
for i in binary_splitter:
    i.strip()
    if length<=len(i):
        length=len(i)
print(length)
    
    


#for i in binary_splitter binary_splitter=binary_s.aplit('0')
