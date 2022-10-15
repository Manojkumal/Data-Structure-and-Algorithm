# function definition
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merged_two_sorted_list(left,right)

def merged_two_sorted_list(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list(b[j])
            j += 1

    while i < len_a:
        sorted_list(a[i])
        i += 1
    
    while j < len_b:
        sorted_list(b[j])
        j += 1
    return sorted_list

if __name__ == "__manin__":
    nums = [50,20,40,30,10]
    print(merge_sort(nums))