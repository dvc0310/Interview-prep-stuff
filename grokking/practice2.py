class Solution(object):
    def canJumpFromPosition(self, position, nums, visitCount):
        if position == len(nums) - 1:
            return True

        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            visitCount[nextPosition] += 1
            if self.canJumpFromPosition(nextPosition, nums, visitCount):
                return True

        return False

    def canJump(self, nums):
        visitCount = [0]*len(nums)
        return self.canJumpFromPosition(0, nums, visitCount), visitCount
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution:
    def __init__(self):
        self.memo = []

    def canJumpFromPosition(self, position, nums):
        if self.memo[position] != 'UNKNOWN':
            return self.memo[position] == 'GOOD'

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(next_position, nums):
                self.memo[position] = 'GOOD'
                return True

        self.memo[position] = 'BAD'
        return False

    def canJump(self, nums):
        self.memo = ['UNKNOWN'] * len(nums)
        self.memo[-1] = 'GOOD'
        return self.canJumpFromPosition(0, nums)
    
class Solution(object):
    def canJump(self, nums):
       targetIndex = len(nums) - 1
       visited = len(nums) * [False]
       visitCount = [0]*len(nums)
       stack = [(0, nums[0])]
       while stack:
          idx, val = stack.pop()
          visitCount[idx] += 1
          if idx == targetIndex:
            return True, visitCount
          if not visited[idx]:
            visited[idx] = True
            jumplength = val + idx + 1
            if jumplength > len(nums):
               jumplength = len(nums)
            for i in range(idx, jumplength):
                stack.append((i, nums[i]))
       return False, visitCount
    
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))




nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution(object):
    def canJump(self, nums):
        memo = ['UNKNOWN'] * len(nums)
        memo[-1] = 'GOOD'
        visited = len(nums) * [0]
        
        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                visited[i] += 1
                if memo[j] == 'GOOD':
                    memo[i] = 'GOOD'
                    break
                    
        return memo[0] == 'GOOD', visited
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))


class Solution(object):
    def canJump(self, nums):
        visited = len(nums) * [0]
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
                visited[i] += 1
        return lastPos == 0, visited
    
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))