class Solution(object):
    def __init__(self):
        self.memo = {}
        
    def wordBreak(self, s, wordDict):
        my_string = ""
        return self.helper(s, wordDict, my_string)
        
    def helper(self, s, wordDict, my_string):
        if my_string in self.memo:
            return self.memo[my_string]
        if my_string == s:
            self.memo[my_string] = True
            return True
        if len(my_string) > len(s):
            self.memo[my_string] = False
            return False
        ab = s[:len(my_string)]
        if ab == my_string:
            for i in range(0, len(wordDict)):
                if self.helper(s, wordDict, my_string + wordDict[i]):
                    self.memo[my_string] = True
                    return True
        self.memo[my_string] = False
        return False

class Solution(object):        
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict)
        
    def helper(self, s, wordDict):
        if s in wordDict:
            return True

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if right in wordDict and self.helper(left, wordDict):
                return True
            
        return False

s = "applepenapplepenapple"
wordDict = ["apple", "pen"]
print(Solution().wordBreak(s, wordDict))
class Solution(object):
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        if s in self.memo:
            return self.memo[s]
        if s in wordDict:
            self.memo[s] = True
            return True

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if right in wordDict and self.helper(left, wordDict):
                self.memo[s] = True
                return True

        self.memo[s] = False
        return False

s = "applepenapplepenapple"
wordDict = ["apple", "pen"]
print(Solution().wordBreak(s, wordDict))

class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] is True if s[:i] can be segmented into words in wordDict

        dp[0] = True  # base case

        for i in range(1, n + 1):
            for word in wordDict:
                word_length = len(word)
                
                if word_length > i:  # the word is too long, go to the next word
                    continue
                
                # Calculate the start index of the substring that we will compare with the word
                start_index = i - word_length 
                
                # Check if the substring is equal to the word
                if s[start_index:i] != word:
                    continue
                
                # If the substring equals the word, check if the remaining string can be segmented
                if dp[start_index] == False:  # the remaining string can't be segmented, go to the next word
                    continue
                
                # If we made it here, both conditions are met: 
                # the substring equals the word and the remaining string can be segmented
                dp[i] = True
                break  # no need to check other words

        return dp[-1]  # return if s can be segmented into words in wordDict


s = "apppen"
wordDict = ["app","pen"]
print(Solution().wordBreak(s, wordDict))