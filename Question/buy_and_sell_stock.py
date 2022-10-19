# function definition
def maxprofit(arr):
    min_price= float('inf')
    max_profit = 0
    for i in range(len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        elif arr[i] - min_price > max_profit:
            max_profit = arr[i] - min_price
    return max_profit








# driver code
arr = [7, 1, 5, 3, 6, 4, 15]
# function calling
result = maxprofit(arr)
print(f"The maximum profit to buy and sell the stock is :{result}")