# function definition
def selection_sorting(arr):
    n = len(arr)
    for i in range(n):
        # to store the minimum elements of the index
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# driver code
arr = [50, 38, 75, 28, 11, 17, 20, 37]

# function definition
result = selection_sorting(arr)
print("The sorted array is ",result)