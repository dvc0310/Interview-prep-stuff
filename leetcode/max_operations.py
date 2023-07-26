class Solution(object):
    def maxOperations(self, nums, k):
        list.sort(nums)
        count = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            else:
                if nums[r] + nums[l] > k:
                    r -= 1
                elif nums[r] + nums[l] < k:
                    l += 1
            
        return count