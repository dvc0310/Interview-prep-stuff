import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                print("square: " + str(square))
                if i < square:
                    break
                nu = i-square
                print("i - square: " + str(nu))
                a = dp[nu] + 1
                print("new: " + str(a) )
                dp[i] = min(dp[i], a)
        
        return dp[-1]
print(Solution().numSquares(12))

class Solution:
  def solve_knapsack(self, profits, weights, capacity):
    
    return self.solve_knapsack_helper(profits, weights, capacity, 0)
  
  def solve_knapsack_helper(self, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0
    
    profit1 = 0

    if weights[index] <= capacity:
      profit1 = profits[index] + self.solve_knapsack_helper(
        profits, weights, capacity - weights[index], index + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = self.solve_knapsack_helper(profits, weights, capacity, index + 1)

    return max(profit1, profit2)
  
weights = [2,3,1,4]
arr = [4,5,3,7]
print(Solution().solve_knapsack(weights, arr, 5))

def ap(arr, target):
    l = 0
    currProd = 1
    lst = []
    for r in range(len(arr)):
        currProd *= arr[r]
        while l <= r and currProd >= target:
            currProd /= arr[l]
            l += 1
        tempProd = 1
        for i in range(r, l-1, -1):
            tempProd *= arr[i]
            lst.append(arr[i:r+1])
            if tempProd >= target:
                break
    return lst



arr = [2, 5, 3, 10]
target=30 
print(ap(arr, target))