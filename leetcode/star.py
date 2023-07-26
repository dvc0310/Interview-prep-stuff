class Solution(object):
    def removeStars(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
        return str.join('', stack)