
## function definition
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
    
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr

## driver code
arr = [9,5,1,4,3]

## function calling
result = insertionSort(arr)
print("The sorted array is ",result)