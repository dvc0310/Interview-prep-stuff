class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        lengths = [1]*len(nums)  # lengths[i] = length of longest ending in nums[i]
        for current in range (1, len(nums)):
            for previous in range(0, current):
                if nums[current] > nums[previous]:
                    if lengths[current] >= lengths[previous]:
                        lengths[current] = lengths[previous] + 1

        return max(lengths)

   
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)
        lengths = [1]*n  
        counts = [1]*n  

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        longest = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == longest)

