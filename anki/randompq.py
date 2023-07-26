import heapq
import random
class randomPQ:
    def __init__(self):
        self.items = []
    
    def sample(self):
        return self.items[random.randint(0, len(self.items) - 1)]
    
    def delRandom(self):
        i = random.randint(0, len(self.items) - 1)
        removed_item = self.items[i]
        self.items[i], self.items[-1] = self.items[-1], self.items[i]
        self.items.pop()
        heapq.heapify(self.items)
        
        return removed_item