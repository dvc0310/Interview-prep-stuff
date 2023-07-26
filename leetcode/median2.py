import heapq
class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.median = None
    
    def insert(self, node):
        if self.median == None:
           self.median = node
           return
       
        if node > self.median:
            heapq.heappush(self.minheap, node)
        else:
            heapq.heappush(self.maxheap, -node)
        
        if len(self.minheap) < len(self.maxheap):
            heapq.heappush(self.minheap, self.median)
            self.median = -heapq.heappop(self.maxheap)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -self.median)
            self.median = heapq.heappop(self.minheap)
        
        
A = [10, 10, 1, -6, 7, 2, 10, -10, -3, -5]
mf = MedianFinder()
for i in A:
    mf.insert(i)

print(mf.median)
print(sorted(A))