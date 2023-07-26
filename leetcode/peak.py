import math
class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
                
        return left

    def minEatingSpeed(self, piles, h):
        low = min(piles)
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            sum = 0
            for num in piles:
                sum += math.ceil(num / mid)
            if sum <= h:
                high = mid
            else:
                low = mid + 1

        return low

nums = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(nums))
piles = [3,6,7,11]
h = 8
piles = [30,11,23,4,20]
h = 5
piles = [30,11,23,4,20]
h = 6
piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))

