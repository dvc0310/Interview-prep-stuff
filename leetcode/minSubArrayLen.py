from collections import deque
class Solution(object):
    def minSubArrayLen(self, target, nums):
        curr_sum = 0
        min_length = float('inf')
        queue = deque()
        for j in range(len(nums)):
            curr_sum += nums[j]
            queue.append(nums[j])
            while curr_sum >= target:
                min_length = min(min_length, len(queue))
                curr_sum -= queue.popleft()
        return min_length

target = 4
nums = [1,4,4]
Solution().minSubArrayLen(target, nums)