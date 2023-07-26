class Solution(object):
    def reverseVowels(self, s):
        def isVowel(char):
            char = char.lower()
            return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
        l = 0
        r = len(s) - 1
        s = list(s)
        while l < r:
            if isVowel(s[l]) and isVowel(s[r]):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif isVowel(s[l]) and not isVowel(s[r]):
                r -= 1
            elif not isVowel(s[l]) and isVowel(s[r]):
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)
