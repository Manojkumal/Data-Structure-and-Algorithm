from collections import Counter
import heapq

# function Definition
def topKfrequentelement(arr,k):
    if k == len(arr):
        return set(arr)
    
    count = Counter(arr)
    return heapq.nlargest(k,count,key=count.get)
    
# Driver Code
arr = [1,1,1,2,2,3]
k = 3

# function calling
result = topKfrequentelement(arr,k)
print("The top k elements is ",result)
