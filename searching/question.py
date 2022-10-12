# Question: Finding  first infinity from array?

def find_infinity_at_first(arr,i,j,x):
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid]!= 'inf':
            return find_infinity_at_first(arr,mid+1,j,x)
        if arr[mid]=='inf':
            if arr[mid-1]!='inf':
                return mid
            else:
                return find_infinity_at_first(arr,i,mid-1,x)
            
arr = [20,-30,-5, -45, 10,5,7,0,29,'inf','inf','inf']
x = 'inf'
i = 0
j = len(arr)-1
result = find_infinity_at_first(arr,i,j,x)
print(f"The first infinite value at {result} index")