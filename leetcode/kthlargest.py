import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        largest = 0
        for i in range(k):
            largest = heapq.heappop(nums)
        return -largest


nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))