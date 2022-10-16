
from heapq import heappop, heappush
import math


# function definition

def get_dist(x,y):
    return math.sqrt(x**2+y**2)

def topKclosestelement(points, k):
    min_heap = []
    n = len(points)
    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        heappush(min_heap, (get_dist(x,y), points[i]))

    result = []
    for j in range(k):
        result.append(heappop(min_heap)[1])
    return result

## driver code
points = [[3,3],[5,-1],[4,-2]]
k = 2

result = topKclosestelement(points,k)
print("k colsest poinsts to the orgin are ",result)





# from heapq import heappop, heappush
# import math


# # function definition

# def get_dist(x,y):
#     return math.sqrt(x**2+y**2)

# def topKclosestelement(points, k):
#     max_heap = []
#     n = len(points)
#     for i in range(n):
#         x = points[i][0]
#         y = points[i][1]
#         heappush(max_heap, (get_dist(x,y), points[i]))

#     result = []
#     for j in range(k):
#         result.append(heappop(max_heap)[1])
#     return result

# ## driver code
# points = [[3,3],[5,-1],[4,-2]]
# k = 2

# result = topKclosestelement(points,k)
# print("k colsest poinsts to the orgin are ",result)