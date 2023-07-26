class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = 0.0
        max_sum = 0.0
        for i in range(k):
            window_sum += nums[i]
            max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
    
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        window_sum = 0.0
        max_sum = 0.0
        for i in range(k):
            if s[i] in vowels:
                window_sum += 1
                max_sum = window_sum
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                window_sum -= 1
            if s[i] in vowels:
                window_sum += 1
            max_sum = max(max_sum, window_sum)
        return max_sum

    
    def longestOnes(self, nums, k):
        left, right = 0, 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

        return right - left + 1




nums = [-1]
k = 1
print(Solution().findMaxAverage(nums, k))
nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))
s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(Solution().longestOnes(nums, 2))
nums = [0, 0, 1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(Solution().longestOnes(nums, k))
nums = [1, 0, 0, 1, 0, 1, 0, 1]
k = 2
print(Solution().longestOnes(nums, k))