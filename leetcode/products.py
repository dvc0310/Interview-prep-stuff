import bisect
class Solution:
    def suggestedProducts(self, A, searchWord):
        A.sort()
        res, cur = [], ''
        for c in searchWord:
            cur += c
            i = bisect.bisect_left(A, cur)
            res.append([w for w in A[i:i+3] if w.startswith(cur)])
        return res

solution = Solution()

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(solution.suggestedProducts(products, searchWord))
# Output: [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]

products = ["havana"]
searchWord = "havana"
print(solution.suggestedProducts(products, searchWord))
# Output: [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
print(solution.suggestedProducts(products, searchWord))
# Output: [['baggage','bags','banner'], ['baggage','bags','banner'], ['bags']]

products = ["havana"]
searchWord = "tatiana"
print(solution.suggestedProducts(products, searchWord))
# Output: [[], [], [], [], [], [], []]
