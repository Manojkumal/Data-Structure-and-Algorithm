# function definition
def bubble_sorting(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


# driver code
arr = [70, 20, 40, 30, 90, 5, 15]

# function calling
result  = bubble_sorting(arr)
print("The sorted array is ",result)
