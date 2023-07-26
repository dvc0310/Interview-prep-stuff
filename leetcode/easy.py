class Solution(object):
    def lengthOfLastWord(self, s):
        end_idx = len(s) - 1
        while end_idx > 0 and s[end_idx] == ' ':
            end_idx -= 1
        count = 0
        print(s[end_idx])
        for i in range(end_idx, -1, -1):
            if s[i] == ' ':
                break
            else:
                count += 1
        return count

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))

class Solution(object):
    def longestCommonPrefix(self, strs):
        letter = ''
        s = ""
        done = False
        for i in range(len(min(strs))):
            for j in range(len(strs)):
                if j == 0:
                    letter = strs[j][i]
                else:
                    if letter != strs[j][i]:
                        done = True
                        break
            if done:
                break
            else:
                s += min(strs)[i]
        return s
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        s = ""
        for i in range(len(haystack)):
            if s == "" and haystack[i] != needle[0]:
                continue
            s += haystack[i]
            if len(s) == n:
                if s == needle:
                    return i - len(s) + 1
                else:
                    s = s[1:]
                    while s[0] != needle[0]:
                        s = s[1:]
        return -1 

haystack = "missiissippi"
needle = "iissi"
print(Solution().strStr(haystack, needle))