class Solution(object):
    def __init__(self):
        self.roman_dict = {
            1 : "I",
            4 : "IV",
            5 : "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
    def intToRoman(self, num):
        s = ""
        while num > 0:
            if num >= 1000:
                num -= 1000
                s += self.roman_dict[1000]
            elif num >= 900:
                num -= 900
                s += self.roman_dict[900]
            elif num >= 500:
                num -= 500
                s += self.roman_dict[500]
            elif num >= 400:
                num -= 400
                s += self.roman_dict[400]
            elif num >= 100:
                num -= 100
                s += self.roman_dict[100]
            elif num >= 90:
                num -= 90
                s += self.roman_dict[90]
            elif num >= 50:
                num -= 50
                s += self.roman_dict[50]
            elif num >= 40:
                num -= 40
                s += self.roman_dict[40]
            elif num >= 10:
                num -= 10
                s += self.roman_dict[10]
            elif num >= 9:
                num -= 9
                s += self.roman_dict[9]
            elif num >= 5:
                num -= 5
                s += self.roman_dict[5]
            elif num >= 4:
                num -= 4
                s += self.roman_dict[4]
            else:
                num -= 1
                s += self.roman_dict[1]
            
        return s
    
print(Solution().intToRoman(1994))

