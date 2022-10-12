# function definition using recursion
def binary_search(arr,i,j,x):
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr,mid+1,j,x)
        else:
            return binary_search(arr,i,mid-1,x)
    return -1


# driver code
arr = [10, 15, 20, 25, 30, 35, 40, 50, 90]
i = 0
j = len(arr) - 1
x = 10
# function calling
result = binary_search(arr,i,j,x)
print(f"The element found at {result} index")



# function definition using recursion
def binary_search(arr,i,j,x):
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid] < x:
            i = mid+1
        else:
            j = mid-1
    return -1


# driver code
arr = [10, 15, 20, 25, 30, 35, 40, 50, 90]
i = 0
j = len(arr) - 1
x = 10
# function Calling
result = binary_search(arr,i,j,x)
print(f"The element found at {result} index")