class Solution(object):
    def compress(self, chars):
        s = ""
        curr = chars[0]
        currcount = 1
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                currcount += 1
            else:
                s += curr
                if currcount > 1:
                    s += str(currcount)
                curr = chars[i]
                currcount = 1
        s += curr
        if currcount > 1:
            s += str(currcount)
        for i in range(0, len(s)):
            chars[i] = s[i]

        return len(s)
    