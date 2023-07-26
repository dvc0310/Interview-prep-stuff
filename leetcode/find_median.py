import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = [] 
        self.median = None 

    def insert(self, key):
        if self.median is None:
            self.median = key
            return
        
        if key <= self.median:
            heapq.heappush(self.max_heap, -key)
        else: 
            heapq.heappush(self.min_heap, key)
        
        if len(self.max_heap) - len(self.min_heap) > 2:
            heapq.heappush(self.min_heap, -self.median)
            self.median = -heapq.heappop(self.max_heap)
        elif len(self.min_heap) - len(self.max_heap) > 2:
            heapq.heappush(self.max_heap, -self.median)
            self.median = heapq.heappop(self.min_heap)

    def find_median(self):
        if self.median is not None:
            return self.median
        else:
            raise Exception("Heap is empty")

    def remove_median(self):
        if self.median is not None:
            result = self.median
            if len(self.max_heap) == 0 and len(self.min_heap) == 0:
                self.median = None
            elif len(self.max_heap) >= len(self.min_heap):
                self.median = -heapq.heappop(self.max_heap)
            else:
                self.median = heapq.heappop(self.min_heap)
            return result
        else:
            raise Exception("Heap is empty")


