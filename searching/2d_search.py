# function definition
from sqlalchemy import false


def search_sort_matrix(matrix,target):
    # number of rows
    m = len(matrix)
    if m == 0:
        return False
    
    # number of columns
    n = len(matrix[0])
    left, right = 0, m*n-1
    while left <= right:
        mid = left + (right - left) // 2
        # row  = index//column
        # column = index % column
        mid_element = matrix[mid//n][mid%n]
        if target == mid_element:
            return True
        if target < mid_element:
            right = mid-1
        else:
            left = mid+1
    return False



# driver code
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# function calling
result = search_sort_matrix(matrix,target)
print("result",result)