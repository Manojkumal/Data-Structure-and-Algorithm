# Implementation of QuickSort
import random
def swap(a,b,arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def Partition(arr,start,end):
    r = random.randint(start,end)
    swap(r,start,arr)
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start<end:
            swap(start, end, arr)
    swap(pivot_index, end, arr)
    return end

def quick_sort(arr,start,end):
    if start < end:
        pi = Partition(arr,start,end) # partition index
        quick_sort(arr,start,pi-1) # the left partition
        quick_sort(arr,pi+1,end) # the right partition
        return arr

# driver code
arr = [11, 9, 29, 7, 2, 15, 28]
start = 0
end = len(arr) - 1
# function call
result = quick_sort(arr,start,end)
print(f"The Sorted Array is {result} ")