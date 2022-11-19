# function defintion
def find_maxima_minima(arr,i,j):
    # for single element - small problem
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    # for more than one element - small problem
    elif i == j-1:
        if arr[i]>arr[j]:
            max_val = arr[i]
            min_val = arr[j]
        else:
            max_val = arr[j]
            min_val = arr[i]

    else:
        mid = i + (j - i) // 2
        max_val1, min_val1 = find_maxima_minima(arr,i,mid)
        max_val2, min_val2 = find_maxima_minima(arr,mid+1,j)

        max_val = max_val1 if max_val1 > max_val2 else max_val2
        min_val = min_val1  if min_val1 < min_val2 else min_val2

    return max_val,min_val

# driver code
arr = [10, 70, 45, 16, 29, 30, 36, 20, 1000, -1000]
i = 0
j = len(arr) - 1
# function calling
max_value,min_value =  find_maxima_minima(arr,i,j)
print("The Maximum and Minimum value in array is ", max_value, min_value)


# Time Complexity: O(logn)
# space Complexity: 0(1)

