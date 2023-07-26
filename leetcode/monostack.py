class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            ans = 1
            while stack and stack[-1][1] < temp:
                idx, _ = stack.pop()
                res[idx] = i - idx
                ans+=stack.pop()[1]
            stack.append((i, temp))
            
        return res



temperatures = [73,74,75,71,69,72,76,73]


print(Solution().dailyTemperatures(temperatures))

from collections import deque
class StockSpanner:

    def __init__(self):
        self.stk = deque()

    def next(self, price):
        ans = 1
        while self.stk and self.stk[-1][0] <= price:
            ans+=self.stk.pop()[1]
        self.stk.append([price,ans])
        return ans
        
        
stockspanner = StockSpanner()
a = [100, 80, 60, 70, 60, 75, 85]
lst = []
for price in a:
    lst.append(stockspanner.next(price))
print(lst)
