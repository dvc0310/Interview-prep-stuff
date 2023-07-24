class Solution:
    def calculateFibonacciMemo(self, n):
        memoize = [-1 for x in range(n+1)]
        return self.calculateFibonacciRecur(memoize, n)


    def calculateFibonacciRecur(self, memoize, n):
        if n < 2:
            return n

        # if we have already solved this subproblem, simply return the result from the cache
        if memoize[n] >= 0:
            return memoize[n]
        left = self.calculateFibonacciRecur(memoize, n - 1)
        right = self.calculateFibonacciRecur(memoize, n - 2)
        memoize[n] = left + right
        return memoize[n]
  
    def calculateFibonacciTab(self, n):
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]
    
    def solve_knapsack(self, profits, weights, capacity):
        return self.knapsack_recursive(profits, weights, capacity, 0)


    def knapsack_recursive(self, profits, weights, capacity, currentIndex):
        # base checks
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + self.knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex + 1)

        # recursive call after excluding the element at the currentIndex
        profit2 = self.knapsack_recursive(profits, weights, capacity, currentIndex + 1)

        return max(profit1, profit2)
            
  
print(Solution().calculateFibonacciMemo(4))
  
print(Solution().calculateFibonacciTab(4))

print(Solution().solve_knapsack([1,6,10,16], [1,2,3,5], 7))