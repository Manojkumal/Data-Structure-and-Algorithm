
# function definition using recursion
def ternary_serach(arr,l,r,target):
    mid1 = l + (r-l) // 3
    mid2 = r - (r-l) //3
    while l <= r:
        if arr[mid1]==target:
            return mid1
        elif arr[mid2]==target:
            return mid2
        elif arr[mid1]>target:
            return ternary_serach(arr,l,mid1-1,target)
        elif arr[mid2]<target:
            return ternary_serach(arr,mid2+1,r,target)
        else:
            return ternary_serach(arr,mid1+1,mid2-1,target)
    return -1

# function defintion using iterative method
def ternary_serach(arr,l,r,target):
    while l <= r:
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) //3
        if arr[mid1]==target:
            return mid1
        elif arr[mid2]==target:
            return mid2
        elif arr[mid1]>target:
            r = mid1-1
        elif arr[mid2]<target:
            l = mid2+1
        else:
            l,r = mid1+1,mid2-1
    return -1
    
# driver code
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target = 3
l = 0
r = len(arr)-1
result = ternary_serach(arr,l,r,target)
print(f"The search element found at {result} index")