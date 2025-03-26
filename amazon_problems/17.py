# k closest points to origin

'''
the first step would be to find the euclidean distance between each point
in the array and the origin and then sort them and then return 
the lowest value in the sorted array, 
if k = 1 then we return 1 number which the least lowest 
if k = 2, we return the least lowest and second least lowest
'''

# the above approach is sorting which has time complexity of O(nlogn)

def kClosest(points,k):
    points.sort(key = lambda p: p[0]**2 + p[1]**2)
    return points[:k]

''' 
the sorting approach is not the best approach, 
we can use heap to solve this problem
which has time complexity of O(nlogk)
'''

import heapq

def kClosest(points,k):
    max_heap = [] # to store k closest points
    
    for (x,y) in points:
        dist = -(x**2 + y**2) # store negative value to make it max heap
        heapq.heappush(max_heap,(-dist,(x,y))) # push (distance, x, y)
        
        if len(max_heap) > k:
            heapq.heappop(max_heap) # pop the largest distance
            
    return [[x,y] for (_, x, y) in max_heap] # extract k closest points
            
        
        
