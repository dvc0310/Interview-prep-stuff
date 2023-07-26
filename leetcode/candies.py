from collections import deque
import heapq
def kidsWithCandies(candies, extraCandies):
    greatest = 0
    i = 0
    queue = []
    lst = len(candies) * [False]
    while i < len(candies):
        if greatest < candies[i]:
            greatest = candies[i]

        if len(queue) == 0:
            heapq.heappush(queue, (candies[i], i))
            lst[i] = True
        elif candies[i] + extraCandies >= greatest:
            heapq.heappush(queue, (candies[i], i))
            lst[i] = True
        
        while queue[0][0] + extraCandies < greatest:
            lst[queue[0][1]] = False
            heapq.heappop(queue)
            
        i += 1
    
    return lst

