class Solution(object):
    def canJump(self, nums):
        lastPos = len(nums) - 1
        my_dict = {}
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                if i + nums[i] <= len(nums) - 1:
                    a = i + nums[i]
                    while a >= i + 1:
                        if i not in my_dict:
                            my_dict[i] = [a]
                        else:
                            my_dict[i].append(a)
                        a -= 1
                lastPos = i
        return lastPos == 0
nums = [2,3,1,1,4]

from collections import deque

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        
        # Start with the first index in the queue
        queue = deque([(0, 0)])  # (index, steps)
        visited = {0}
        
        while queue:
            index, steps = queue.popleft()
            for i in range(index + nums[index], index, -1):
                if i >= len(nums) - 1:
                    return steps + 1
                if i not in visited:
                    visited.add(i)
                    queue.append((i, steps + 1))
        
        return 0


    
nums = [2,3,1,1,4]

class Solution:
    def jump(self, nums):
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0
        
        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far
                
        return answer
    
nums = [2,3,1,1,4]
class Solution:
    def jump(self, nums):
        # The starting range of the first jump is [0, 0]
        jump, n = 0, len(nums)
        cur_end, cur_far = 0, 0
        
        for i in range(n-1):
            if nums[i] + i > cur_far:
                cur_far = nums[i] + i
            
            if i == cur_end:
                cur_end = cur_far
                jump += 1
                
                
        return jump
    


class Solution(object):
    def hIndex(self, citations):
        list.sort(citations)
        maxH = 0
        for i in range(len(citations)):
            maxH = max(min(citations[i], len(citations) - i), maxH)   
        return maxH

class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        papers = [0] * (n + 1)  # papers[i] is the number of papers with i citations.
        for c in citations:
            papers[min(n, c)] += 1  # All papers with citations more than n are considered as n.
        i = n
        s = papers[n]  # sum of papers with citations more than i
        while i > s:
            i -= 1
            s += papers[i]
        return i


# Output: 5
citations = [6,7,5,3,5,6,4,8]
print("H index: " + str(Solution().hIndex(citations)))
# Output: 4
citations = [10,8,5,4,3] 
print("H index: " + str(Solution().hIndex(citations)))
citations = [100]
print("H index: " + str(Solution().hIndex(citations)))
citations = [11,15]
print("H index: " + str(Solution().hIndex(citations)))
citations = [50] * 10000 
print("H index: " + str(Solution().hIndex(citations)))
citations = [1, 7, 9, 4]
print("H index: " + str(Solution().hIndex(citations)))
citations = [0,0,0,0,0,0,0,0,0,0, 1000]
print("H index: " + str(Solution().hIndex(citations)))
citations = []
print("H index: " + str(Solution().hIndex(citations)))

import random
class RandomizedSet(object):

    def __init__(self):
        self.set_num = {}
        self.lst = []
        

    def insert(self, val):
        if val in self.set_num:
            return False
        self.lst.append(val)
        self.set_num[val] = len(self.lst) - 1
        return True
        

    def remove(self, val):
        if val not in self.set_num:
            return False
        last_idx = len(self.lst) - 1
        del_idx = self.set_num[val]
        last_element = self.lst[-1]
        self.lst[del_idx], self.lst[last_idx] = self.lst[last_idx], self.lst[del_idx]
        self.set_num[last_element] = del_idx
        self.set_num.pop(val)
        self.lst.pop()
        return True
        

    def getRandom(self):
        return random.choice(self.lst)

rs = RandomizedSet()
for i in range(10):
    rs.insert(random.randint(0,10))
for i in range(5):
    rs.remove(random.randint(0,10))
rs.getRandom()

class Solution:
    def canCompleteCircuit(self, gas, cost) :
        total_gain = 0
        curr_gain = 0
        answer = 0
        
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1
        
        return answer if total_gain >= 0 else -1

gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1] 
print(Solution().canCompleteCircuit(gas, cost))

class Solution(object):
    def convert(self, s, numRows):
        my_dict = {}
        for i in range(0, numRows):
            my_dict[i] = []
        
        i = 0
        done = False
        while i < len(s):
            tracker = 0
            while tracker < numRows:
                my_dict[tracker].append(s[i])
                i += 1
                tracker += 1
                if i >= len(s):
                    done = True
                    break
            if done:
                break
                
            tracker -= 2
            while tracker > 0:
                my_dict[tracker].append(s[i])
                i += 1
                tracker -= 1
                if i >= len(s):
                    done = True
                    break
            if done:
                break

        return ''.join([char for sublist in my_dict.values() for char in sublist])
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

s = "PAYPALISHIRING"
numRows = 1
print(Solution().convert(s, numRows))


class Solution(object):
    def shiftingLetters(self, s, shifts):
        s = list(s)
        sum_lst = [0] * len(s)
        sum_tracker = 0

        for i in range(len(shifts) - 1, -1, -1):
            sum_tracker += shifts[i]
            sum_lst[i] = sum_tracker

        for i in range(len(shifts)):
            num = ord(s[i]) + sum_lst[i] % 26
            if num > 122:
                num = 97 + num % 123
            s[i] = chr(num)

        return ''.join(s)
s = "wxyz"
shifts = [1,2,3,1]
print(Solution().shiftingLetters(s, shifts))