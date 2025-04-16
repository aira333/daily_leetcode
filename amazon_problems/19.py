# find median from datastream

# we could do sorting but that is not an efficient solution, since it's time complexity is going to get complex

# we will heap data structure to optimize the solution

# for heap, adding and removing elements it's always going to be o(logn)

# find max and min value from max heap and min heap respectively is going to be o(1) much better than o(n)

''' the conditions are :
> smallHeap = MaxHeap (we always want maximum value from the small heap)
> LargeHeap = MinHeap (we always want minimum value from the large heap)

> The length of small heap should be approximately equal to the large heap and vice versa
> The max value in small heap should always be less than or equal to the min value in Large heap, if it's not we pop the max value in heap and add it to the large heap and vice versa
> If the length of small heap exceeds the large heap, we take the max value of small heap and add it to large heap and vice versa
> finally, after balancing the heaps, we take the max value of small heap and min value of large heap and find the median by calculating the average value of the two values

'''
import heapq 

class MedianFinder(object):

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # balance the heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self):
        if len(self.small) == len(self.large):
            return(-self.small[0] + self.large[0]) / 2.0
        else:
            return -self.small[0]