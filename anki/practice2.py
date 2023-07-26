import heapq
class Solution(object):
    def mergeIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        lst = [intervals[0]]

        for i in range(1, len(intervals)):
            last = lst[-1]
            if intervals[i][0] <= last[1]:
                last[1] = max(intervals[i][1], last[1])
            else:
                lst.append(intervals[i])
        return lst
    
    def mergesort(self, arr, l, r):
        if len(arr) <= 1:
            return arr, 0
        m = (l+r) // 2
        left, left_inv = self.mergesort(arr, l, m)
        right, right_inv = self.mergesort(arr, m+1, r)
        merged, merged_inv = self.merge(left, right) 
        return merged, left_inv + right_inv + merged_inv
    
    def merge(self, left, right):
        l = 0
        r = 0
        inv = 0
        arr = []
        while l < len(left) and r < len(right):
            if left[l] >= right[r]:
                arr.append(left[l])
                l += 1
            else:
                arr.append(right[r])
                r += 1
                inv += len(left[l:])
        arr.extend(left[l:])
        arr.extend(right[r:])

        return arr, inv

    def guess(num):
        picked_number = 10  # change to whatever number you picked
        if num > picked_number:
            return -1
        elif num < picked_number:
            return 1
        else:
            return 0

    def guessNumber(self, n):
        l = 1
        r = n
        while l <= r:
            m = (l+r)//2
            if self.guess(m) == 1:
                l = m + 1
            elif self.guess(m) == -1:
                r = m - 1
            else:
                return m
        return m

    def successfulPairs(self, spells, potions, success):
        potions = sorted(potions)
        lst = []
        for num in spells:
            index = self.binarySearch(num, potions, success)
            lst.append(len(potions) - index)
        return lst

    def binarySearch(self, num, potions, success):
        l = 0
        r = len(potions) - 1
        while l <= r:
            m = l + (r - l) // 2
            if potions[m] * num < success:
                l = m + 1
            else:
                r = m - 1
        return l

    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1
    
    def triplet(self, nums):
        first = float('inf')
        second = float('inf')

        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        
        return False
    
    def kthLargest(self, arr, k):
        lst = []
        for i in range(len(arr)):
            lst.append(-arr[i])
        heapq.heapify(lst)
        curr = float('inf')

        while k > 0:
            curr = heapq.heappop(lst)
            k -= 1
        
        return -curr
  

    def kthLargest2(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
    
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


    def longestSubstring(self, s, k):
        def helper(s, start, end, k):
            count = {}
            for i in range(start, end):
                count[s[i]] = count.get(s[i], 0) + 1
            for i in range(start, end):
                if count[s[i]] < k:
                    return max(helper(s, start, i, k), helper(s, i+1, end, k))
            return end - start

        return helper(s, 0, len(s), k)


    def longestSubstring2(self, s: str, k: int) -> int:
        res = 0
        for uniqueTarget in range(1, 27):  # 26 characters from a to z
            countMap = [0]*26
            unique = 0
            countAtLeastK = 0
            left = 0
            right = 0
            while right < len(s):
                if unique <= uniqueTarget:
                    idx = ord(s[right]) - ord('a')
                    if countMap[idx] == 0:
                        unique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k:
                        countAtLeastK += 1
                    right += 1
                else:
                    idx = ord(s[left]) - ord('a')
                    if countMap[idx] == k:
                        countAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0:
                        unique -= 1
                    left += 1

                if unique == uniqueTarget and unique == countAtLeastK:
                    res = max(right - left, res)

        return res
    

    def reverse_vowels(self, s):
        l = 0
        r = len(s) - 1
        vowels = set('aeiouAEIOU')
        s = list(s)
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)
    
    def isPalindrome(self, s):
        x = ''.join(c for c in s.lower() if c.isalpha() or c.isdigit())
        l = 0
        r = len(x) - 1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1

        return True

    def isAnagram(self, s, t):
        return set(s) == set(t) and len(s) == len(t)
    
    def shortestDistance(self, words, word1, word2):
        s1 = 0
        s2 = float('inf')
        min_dist = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                s1 = i
            elif words[i] == word2:
                s2 = i
            min_dist = min(min_dist, abs(s1-s2))
        return min_dist
    
    def numGoodPairs(self, nums):
        pairCount = 0
        lst = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    pairCount += 1
                    lst.append((i, j))

        return pairCount



s = "aaabb"
k = 3
s = "heaaaaaaaaabajbbcacaf"
k = 2
st = "AEIOU"
sentence = "Was it a car or a cat I saw?"
s = "listen"
t = "silent"
words = ["a", "c", "d", "b", "a"]
word1 = "a"
word2 = "b"
nums = [1,2,3,1,1,3]
print(Solution().numGoodPairs(nums))
print(Solution().shortestDistance(words, word1, word2))
print(Solution().isAnagram(s, t))
print(Solution().isPalindrome(sentence))
print(Solution().reverse_vowels(st))
print(Solution().longestSubstring2(s, k))
intervals = [[7,10],[2,4]]
print(Solution().canAttendMeetings(intervals))
nums = [1,7,3,6,5,6]
print(Solution().lengthOfLIS(nums))
print(Solution().kthLargest(nums, 2))
print(Solution().kthLargest2(nums, 2))


nums = [1,7,3,6,5,6]
print(Solution().triplet(nums))


print(Solution().pivotIndex(nums))
nums = [-1,-1,0,1,1,0]
print(Solution().pivotIndex(nums))
nums = [-1,-1,0,1,1,-1]
print(Solution().pivotIndex(nums))
nums = [-1,-1,0,1,1,1]
print(Solution().pivotIndex(nums))