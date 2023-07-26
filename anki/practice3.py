def prodArray(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)

    prefix[0] = 1
    suffix[-1] = 1

    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] * nums[i-1]
    for i in range(len(suffix) - 2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    newArr = []

    for i in range(len(nums)):
        newArr.append(prefix[i] * suffix[i])

    return newArr

def mergeIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    last = intervals[0]
    lst = []

    for i in range(1, len(intervals)):
        if intervals[i][0] <= last[1]:
            last[1] = max(intervals[i][1], last[1])
        else:
            lst.append(last)
            last = intervals[i]
    lst.append(last)  
    return lst

def coinArrange(n):
    return



print(prodArray([1,2,3,4]))
intervals = [[1,3],[2,6],[8,10],[15,18]]
mergeIntervals(intervals)
intervals = [[1,4],[4,5]]
mergeIntervals(intervals)


import heapq
class SmallestInfiniteSet(object):
    def __init__(self):
        self.count = 1
        self.heap = []
        self.set = set()
        
    def popSmallest(self):
        if len(self.heap) > 0:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)
        else:    
            smallest = self.count
            self.count += 1
            
        return smallest
        
    def addBack(self, num):
        if num < self.count and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)

import heapq
class SmallestInfiniteSet(object):
    def __init__(self):
        self.count = 1
        self.heap = []
        self.s = set()
        
    def popSmallest(self):
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.s.remove(smallest)
        else:
            smallest = self.count
            self.count += 1
        return smallest
        
    def addBack(self, num):
        if num < self.count and num not in self.s:
            heapq.heappush(self.heap, num)
            self.s.add(num)


infset = SmallestInfiniteSet()
print(infset.popSmallest())
print(infset.popSmallest())
print(infset.popSmallest())
print(infset.addBack(9))
print(infset.addBack(1))
print(infset.popSmallest())
print(infset.popSmallest())
print(infset.popSmallest())


