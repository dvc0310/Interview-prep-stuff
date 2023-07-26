class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        w1 = sorted(word1)
        w2 = sorted(word2)
        d1 = {}
        d2 = {}
        for i in range(len(w1)):
            if w1[i] not in d1:
                d1[w1[i]] = 1
            else:
                d1[w1[i]] += 1
            if w2[i] not in d2:
                d2[w2[i]] = 1
            else:
                d2[w2[i]] += 1

        lst1 = []
        lst2 = []

        for _, value in d1.items():
            lst1.append(value)
            
        for _, value in d2.items():
            lst2.append(value)

        if sorted(lst1) == sorted(lst2):
            return True
        
        return False

     
word1 = "cabbba"
word2 = "abbccc"

print(Solution().closeStrings(word1, word2))