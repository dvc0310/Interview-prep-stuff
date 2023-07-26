def mostWater(height):
    max_area = 1
    l = 0
    r = len(height) - 1
    while l < r:
        max_area = max(max_area, min(height[r], height[l]) * (r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(mostWater(height))

def singleNumber(nums):
    res = 0
    for num in nums:
        res = num ^ res
    return res
class Solution:
    def longestK(self, s, k):   
        self.memo = {}    
        self.longestK_helper(s,k)
        return self.longest_true_word(self.memo)

    def longest_true_word(self, dictionary):
        max_length = 0
        longest_word = ""
        
        for word, flag in dictionary.items():
            if flag is True and len(word) > max_length:
                max_length = len(word)
                longest_word = word
                
        return longest_word

    def longestK_helper(self, s, k):
        if len(s) == 1:
            return s
        
        if s in self.memo:
            if not self.memo[s]:
                return ""
            else:
                return s

        if not self.check_letter_frequency(s, k):
            self.memo[s] = False
        else:
            self.memo[s] = True
        
        left = self.longestK_helper(s[:len(s) - 1], k)
        right = self.longestK_helper(s[1:], k)
        if len(left) > len(right):
            return left
        else:
            return right

    def check_letter_frequency(self, input_string, threshold):
        letter_count = {}
        for letter in input_string:
            if letter.isalpha():
                if letter.lower() not in letter_count:
                    letter_count[letter.lower()] = 1
                else:
                    letter_count[letter.lower()] += 1

        # Check if all letter counts meet or exceed the threshold
        for count in letter_count.values():
            if count < threshold:
                return False
                
        return True

class Solution2(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return ""

        frequency = [0]*26
        for i in range(len(s)):
            frequency[ord(s[i])-ord('a')] += 1

        for i in range(len(s)):
            if frequency[ord(s[i])-ord('a')] < k:
                # find the max length substring
                substrings = s.split(s[i])
                longest_substring = max(substrings, key=lambda substr: self.longestSubstring(substr, k))
                return self.longestSubstring(longest_substring, k)

        return s

    
text = "aabbbccddeeefffgg"

class Solution3:
    def longestSubstring(self, s, k):
        # Inserting frequency of all characters in map
        mp = {}
        for it in s:
            if it not in mp:
                mp[it] = 1
            else:
                mp[it] += 1

        ind = 0
        # First index of character which has frequency less than k
        while ind < len(s) and mp[s[ind]] >= k:
            ind += 1

        if ind == len(s):
            return len(s)
        # Answer must be in the left part or right part
        left = self.longestSubstring(s[:ind], k)
        right = self.longestSubstring(s[ind + 1:], k)
        return max(left, right)


print(Solution2().longestSubstring(text, 3))
print(Solution3().longestSubstring(text, 3))
print(Solution().longestK(text, 3))

class Solution:
    def longestSubarray(self, nums):
        prev = 0
        curr = 0
        ans = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                ans = max(ans, curr + prev)
                prev = curr
                curr = 0
        ans = max(ans, curr + prev)

        return ans-1 if ans == len(nums) else ans

print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))