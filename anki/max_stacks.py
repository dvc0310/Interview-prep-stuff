import heapq
import random
class MaxStack:
    def __init__(self):
        self.stack = []
        self.currMax = 0
        self.max = []

    def getMax(self):
        return self.currMax
    
    def push(self, n):
        if n > self.currMax:
            self.currMax = n
        self.max.append(self.currMax)
        self.stack.append(n)

    def pop(self):
        val = self.stack.pop()
        self.max.pop()
        if val == self.currMax:
            self.currMax = self.max[-1]
        return val
    