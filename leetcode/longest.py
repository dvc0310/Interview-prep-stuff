class Solution(object):
    def longestSubarray(self, nums):
        l = 0
        r = 0

        while r < len(nums) and nums[l] != 1 :
            l += 1
            r += 1
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1

        if count == len(nums):
            return len(nums) - 1

        if r == len(nums):
            return 0
        
        usedZero = False
        maxlength = 0

        while r < len(nums):
            if (usedZero == True and nums[r] == 0):
                maxlength = max(maxlength, r - l - 1)
                l += 1
                while nums[l - 1] != 0 and l < len(nums):
                    l += 1
                if nums[l] == 0:
                    r = l
                    while l < len(nums) - 1 and nums[l] == 0:
                        l += 1
                        r += 1
                    usedZero = False
            elif usedZero == False and nums[r] == 0:
                usedZero = True
                
            r += 1

        if (nums[r-1] == 1 ):
            if usedZero:
                maxlength = max(maxlength, r - l - 1)
            else:
                maxlength = max(maxlength, r - l)
        if (nums[r-1] == 0):
            maxlength = max(maxlength, r - l - 1)
        

        return maxlength

nums = [0,1,1,1,0,0,1,1,0,1,1,1,1]
nums = [0,1,0]
print(Solution().longestSubarray(nums))