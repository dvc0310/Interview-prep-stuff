class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        st = ""
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                st += s[i]
                i += 1
            j += 1
        if s == st:
            return True
        return False