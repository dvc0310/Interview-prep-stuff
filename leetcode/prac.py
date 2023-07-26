class Solution():
    def threesumClosest(self, nums, target):
        closestSumSoFar = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        for i in range(len(nums)):
            r = len(nums) - 1
            l = i + 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if abs(currentSum - target) < abs(closestSumSoFar - target):
                    closestSumSoFar = currentSum
                if currentSum > target:
                    while nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif currentSum < target:
                    while nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                else:
                    return currentSum
                
        return closestSumSoFar
    

nums = [-1,2,1,-4]
target = 1
print(Solution().threesumClosest(nums, target))

class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        if not self.stack:
            self.stack.push((val, val))
        
        if self.stack[-1][1] > val:
            self.stack.push((val, val))
        else:
            self.stack.push((val, self.stack[-1][1]))
            
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
          
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None
        
class Solution():
    def maxSquare(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        dp = [(col + 1) * [0] for _ in range(row + 1)]
        maxSoFar = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c], dp[r][c]) + 1
                    maxSoFar = max(maxSoFar, dp[r+1][c+1])
        return maxSoFar

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

Solution().maxSquare(matrix)

class Solution():
    def coins(self, n):
        l = 0
        r = n
        
        while l <= r:
            m = (l+r) // 2
            x = m * (m + 1) // 2
            if x > n:
                r = m - 1
            else:
                l = m + 1
        return r
    def longestSub(self, s):
        lst = []
        char_set = set()
        l = 0
        r = 1
        char_set.add(s[l])
        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
            else:
                lst.append(r - l)
                while l < r and s[l-1] != s[r]:
                    l += 1
            r += 1
        return max(lst)
    
Solution().coins(8)
s = "abcabcbb"
print(Solution().longestSub(s))

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1], m = nums1[m-1], m - 1
            else:
                nums1[m+n-1], n = nums2[n-1], n - 1
        if n > 0:
            nums1[:n] = nums2[:n]

nums1 = [-1,0,0,0]
m = 1
nums2 = [-2,-1,0]
n = 3
print(Solution().merge(nums1, m, nums2, n))

class Solution:
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
    
nums = [3,2,2,3]
val = 3
Solution().removeElement(nums, 3)

class Solution(object):
    def removeDuplicates(self, nums):
        numset = sorted(list(set(nums)))
        for i in range(len(numset)):
            nums[i] = numset[i]
        
        return len(numset)
        
     
nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)

class Solution(object):
    def removeDuplicates(self, nums):
        numsmap = {}
        for num in nums:
            if num not in numsmap:
                numsmap[num] = 1
            else:
                if numsmap[num] < 2:
                    numsmap[num] += 1
        i = 0
        for key in sorted(list(numsmap.keys())):
            while numsmap[key] > 0:
                numsmap[key] -= 1
                nums[i] = key
                i += 1
        return i
            
            
        
        
nums = [1,1,1,2,2,3]
Solution().removeDuplicates(nums)

class Solution(object):
    def majorityElement(self, nums):
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        maj, maj_percent = 0, 0.0
        for key in nums_map.keys():
            if float(nums_map[key] / len(nums)) > maj_percent:
                maj = key
                maj_percent = float(nums_map[key] / len(nums))
        
        return maj

nums = [3,2,3]
Solution().majorityElement(nums)


class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        templst = nums[len(nums) - k:]
        
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i-k]
            
        i = 0
        
        while i < k and i < len(templst):
            nums[i] = templst[i]
            i += 1
        
        
nums = [1,2]
k = 3
Solution().rotate(nums, k)

class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        maxSoFar = 0
        while r < len(prices):
            maxSoFar = max(maxSoFar, prices[r] - prices[l])
            while prices[l] > prices[r]:
                l += 1
            r += 1
        return prices
            
nums = [7,1,5,3,6,4]            
Solution().maxProfit(nums)

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
    
class Solution(object):
    def maxProfit(self, prices, fee):
        current_balance = 0
        balance_after_buy = -prices[0]

        for i in range(1, len(prices)):
            previous_balance = current_balance

            balance_if_sell_today = balance_after_buy + prices[i] - fee
            if balance_if_sell_today > current_balance:              
                current_balance = balance_if_sell_today

            balance_if_buy_today = previous_balance - prices[i]
            if balance_if_buy_today > balance_after_buy:
                balance_after_buy = balance_if_buy_today
            
        return current_balance


nums = [7,1,5,3,1,6,4]       
Solution().maxProfit(nums, 0)

def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 0
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

def make_squares(arr):
  n = len(arr)
  squares = [0 for _ in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] ** 2
    rightSquare = arr[right] ** 2
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares


print("Squares: " + str(make_squares([ -1,-2, -3])))
print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


class Solution:
    def three_sum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result

#print(Solution().three_sum([-5, 2, -1, -2, 3]))



def two_sum_hash_table(arr, total):
    hash_table = dict()

    for i in range(len(arr)):
        complement = total - arr[i]
        if complement in hash_table:
            return (i, hash_table[complement])
        else:
            hash_table[arr[i]] = i
    return None

two_sum_hash_table(arr = [2,7,11,15], total = 9)

def triplets(nums, target):
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < target:
                result.append((nums[i], nums[l], nums[r]))
                l += 1
            else:
                r -= 1
    
    return result

def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0: 
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return result


arr = [-1, 4, 2, 1, 3]
target= 5 
triplets(arr, target)

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        left, right = i + 1, len(arr) - 1
        while (left < right):
            if arr[i] + arr[left] + arr[right] < target:  
                # since arr[right] >= arr[left], we replace arr[right] by any number between 
                # left and right to get a sum less than the target sum
                for k in range(right, left, -1):
                    triplets.append([arr[i], arr[left], arr[k]])
                left += 1
            else:
                right -= 1  # we need a pair with a smaller sum
    return triplets
#print(triplet_with_smaller_sum(arr, target))

from collections import deque
import copy
class Solution:
  def findSubarrays(self, arr, target):
    result = []
    dq = deque()
    prod = 1
    for num in arr:
        if not dq:
            dq.append(num)
            prod = prod * num
            if prod < target:
                result.append(list(dq))
        else:
            if prod * num < target:
                dq.append(num)
                prod = prod * num
                result.append(list(dq))
            else:
                while list(dq) and prod * num >= target:
                    div = dq.popleft()
                    prod = prod // div
                    if list(dq) and prod < target:
                        result.append(list(dq))  
                dq.append(num)
                prod = prod * num
                if prod < target:
                    result.append(list(dq))
    if [arr[-1]] not in result:
        result.append([arr[-1]])
    return result

#print(Solution().findSubarrays([1, 2, 3, 4, 5], 10))

def find_subarrays(arr, target):
    result = []
    product = 1.0
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        temp_list = []
        for i in range(right, left - 1, -1):
            temp_list.insert(0, arr[i])
            result.append(list(temp_list))
    return result


class Solution:
    def findSubarrays(self, arr, target):
        result = []
        dq = deque()
        prod = 1
        for num in arr:
            # While the product is not less than target, pop elements from deque
            while dq and prod * num >= target:
                prod //= dq.popleft()
            
            # Append the current number to deque and also to the result if product is less than target
            dq.append(num)
            prod *= num
            
            if prod < target:
                # Append all subarrays ending at current number to the result
                temp = deque()
                for i in range(len(dq)-1, -1, -1):
                    temp.appendleft(dq[i])
                    result.append(list(temp))
                
        return result

# Example usage
#print(find_subarrays([2, 5, 3, 10], 30))
#print(find_subarrays([8, 2, 6, 5], 50))

class Solution:
    def hasCycle(self, matrix):
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if visited[row][col] == 0 and self.dfs(matrix, row, col, visited, None):
                    return True
        return False

    def dfs(self, matrix, row, col, visited, parent):
        stack = [(row, col, False, parent)]
        hasCycle = False
        while stack:
            y, x, backtrack, parent = stack.pop()
            if backtrack:
                visited[y][x] = 2
            else:
                if visited[y][x] == 0:
                    visited[y][x] = 1
                    stack.append((y, x, True, None))
                    for neighbor in self.neighbors(matrix, y, x):
                        if (neighbor[0], neighbor[1]) != parent:
                            stack.append((neighbor[0], neighbor[1], False, (y, x)))
                elif visited[y][x] == 1:
                    hasCycle = True
        return hasCycle

    def neighbors(self, matrix, row, col):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == matrix[row][col]:
                yield new_row, new_col
                
class Solution(object):
    def minimumCardPickup(self, cards):
        hashmap = {}
        i = 0
        for i in range(len(cards)):
            if cards[i] not in hashmap:
                hashmap[cards[i]] = [i]
            else:
                hashmap[cards[i]].append(i)
                
        lower, upper = float('-inf'), float('inf')
        
        for key in hashmap.keys():
            if len(hashmap[key]) > 1:
                for i in range(1, len(hashmap[key])):
                    if abs(hashmap[key][i - 1] - hashmap[key][i]) < (upper - lower):
                        lower = min(hashmap[key][i - 1], hashmap[key][i])
                        upper = max(hashmap[key][i - 1], hashmap[key][i])
        if upper == float('inf'):
            return - 1
        return upper - lower + 1        
    
class Solution(object):
    def minimumCardPickup(self, cards):
        hashmap = {}
        min_length = float('inf')

        for i, card in enumerate(cards):
            if card in hashmap:
                min_length = min(min_length, i - hashmap[card])
            hashmap[card] = i

        if min_length == float('inf'):
            return -1
        return min_length + 1

        
cards = [3,4,2,3,4,7]
#print(Solution().minimumCardPickup(cards))

def uniquePaths(m, n):
    # Initialize a 2D list with -1s indicating that these cases have not been computed yet.
    memo = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        memo[i][0] = 1
    for j in range(n):
        memo[0][j] = 1

    # Define the function that uses this 2D list.
    def paths(m, n):
        if m == 0 or n == 0:
            return 1
        if memo[m][n] != -1:
            return memo[m][n]
        else:
            vertical = paths(m - 1, n)
            horizontal = paths(m, n - 1)
            memo[m][n] = vertical + horizontal
            return memo[m][n]

    return paths(m - 1, n - 1)  # Subtract 1 to adjust for 0-indexing.

def uniquePaths(m, n):
    # If you're at the end point, there's only one path.
    if m == 1 or n == 1:
        return 1
    # If you're not at the end point, the number of unique paths will be the sum of 
    # the number of unique paths from the point to the right and the point below.
    else:
        return uniquePaths(m-1, n) + uniquePaths(m, n-1)


print(uniquePaths(3, 7))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize DP table
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Fill the first column with 1s
        for i in range(m):
            dp[i][0] = 1
        
        # Fill the first row with 1s
        for j in range(n):
            dp[0][j] = 1
        
        # Use the recurrence relation to fill the rest of the table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the number of unique paths to the last cell
        return dp[m-1][n-1]
print(Solution().uniquePaths(3, 7))
class Solution:
    def solve_knapsack(self, profits, weights, capacity):
        self.memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]
        result = self.helper(profits, weights, capacity, 0)
        for i in range(len(profits) + 1):
            for j in range(capacity + 1):
                if self.memo[i][j] == -1:
                    self.memo[i][j] = 0
        print(self.memo)
        return result

    def helper(self, profits, weights, capacity, currentIndex):
        # base checks
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        if self.memo[currentIndex][capacity] != -1:
            return self.memo[currentIndex][capacity]
        
        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + self.helper(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
        
        # recursive call after excluding the element at the currentIndex
        profit2 = self.helper(profits, weights, capacity, currentIndex + 1)
        max_profit = max(profit1, profit2)
        self.memo[currentIndex][capacity] = max_profit
        return max_profit


#print(Solution().solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

class Solution:
    def solve_knapsack(self, profits, weights, capacity):
        # create a dp table for memoization
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]

        # iterate through all profits/weights
        for currentIndex in range(1, len(profits) + 1):
            for currentCapacity in range(1, capacity + 1):
                profit1 = 0
                profit2 = 0

                # recursive call after choosing the element at the currentIndex
                # if the weight of the element at currentIndex exceeds the currentCapacity, we shouldn't process this
                if weights[currentIndex - 1] <= currentCapacity:
                    profit1 = profits[currentIndex - 1] + dp[currentIndex - 1][currentCapacity - weights[currentIndex - 1]]
                
                # recursive call after excluding the element at the currentIndex
                profit2 = dp[currentIndex - 1][currentCapacity]

                dp[currentIndex][currentCapacity] = max(profit1, profit2)
        print(dp)
        return dp[len(profits)][capacity]


#print(Solution().solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

