class Solution(object):
    def reverseWords(self, s):
        res = s.split()
        rev = ""
        for index, element in enumerate(reversed(res)):
            rev += element
            if index < len(res):
                rev += " "
        return rev
