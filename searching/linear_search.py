
# function definition
def linear_search(arr,x):
    for i in range(len(arr)):
        if x==arr[i]:
            return i


# dirver code
arr = [8,5,2,9,4,10,30,20,15,14]
x = 10

# function calling
result = linear_search(arr,x)
print(f"The search element found at {result} index")