class Solution(object):

    def __init__(self):
        self.my_dict = {'I': 1,  'V': 5, 'X': 10, 'L': 50, 
    'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        sum = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if s[i] == 'I' and s[i+1] == 'X':
                    sum += 9
                    i += 2
                elif s[i] == 'I' and s[i+1] == 'V':
                    sum += 4
                    i += 2
                elif s[i] == 'X' and s[i+1] == 'L':
                    sum += 40
                    i += 2
                elif s[i] == 'X' and s[i+1] == 'C':
                    sum += 90
                    i += 2
                elif s[i] == 'C' and s[i+1] == 'D':
                    sum += 400
                    i += 2
                elif s[i] == 'C' and s[i+1] == 'M':
                    sum += 900
                    i += 2
                else:
                    sum += self.my_dict[s[i]]
                    i += 1
            else:
                sum += self.my_dict[s[i]]
                i += 1
        return sum

