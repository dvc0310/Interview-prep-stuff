def binary_search(arr, key):
  start, end = 0, len(arr) - 1
  isAscending = arr[start] < arr[end]
  while start <= end:
    # calculate the middle of the current range
    mid = start + (end - start) // 2

    if key == arr[mid]:
      return mid

    if isAscending:  # ascending order
      if key < arr[mid]:
        end = mid - 1  # the 'key' can be in the first half
      else:  # key > arr[mid]
        start = mid + 1  # the 'key' can be in the second half
    else:  # descending order
      if key > arr[mid]:
        end = mid - 1  # the 'key' can be in the first half
      else:  # key < arr[mid]
        start = mid + 1  # the 'key' can be in the second half

  return -1  # element not found


def search_ceiling_of_a_number(arr, key):
  n = len(arr)
  if key > arr[n - 1]:  # if the 'key' is bigger than the biggest element
    return -1

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:  # found the key
      return mid

  # since the loop is running until 'start <= end', so at the end of the while loop, 
  # 'start == end+1' we are not able to find the element in the given array, so the next
  # big number will be arr[start]
  return start

def search_next_letter(letters, key):
  n = len(letters)

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < letters[mid]:
      end = mid - 1
    else: # key >= letters[mid]:
      start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 
  # 'start == end+1'
  return letters[start % n]

def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares

class Solution:
    def findRange(self, arr, key):
        result = [- 1, -1]
        index = self.binary_search(arr, key)
        if index == -1:
          return result
        upper = index
        lower = index
        for i in range(index + 1, len(arr)):
            if arr[i] != key:
              break
            else:
              upper += 1
        for i in range(index - 1, -1, -1):
            if arr[i] != key:
              break
            else:
              lower -= 1
        result = [lower, upper]
        return result
    def binary_search(self, arr, key):
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == key:
              return m
            elif arr[m] > key:
              r = m - 1
            else:
              l = m + 1
        return -1
arr = [1, 3, 8, 10, 15]
key = 12
print(Solution().findRange(arr, key))

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1
  return nums

print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum > target:
                r -= 1
            else:
                l += 1
        return [l, r]
numbers = [0,0,3,4]
target = 0
print(Solution().twoSum(numbers, target))

class Solution(object):
    def canJump(self, nums):
        targetIndex = len(nums) - 1
        return self.dfs(nums, targetIndex)
    def dfs(self, nums, targetIndex):
       visited = len(nums) * [False]
       stack = [(0, nums[0])]
       while stack:
          idx, val = stack.pop()
          if idx == targetIndex:
            return True
          if not visited[idx]:
            visited[idx] = True
            jumplength = val + idx + 1
            if jumplength > len(nums):
               jumplength = len(nums)
            for i in range(idx, jumplength):
               if not visited[i]:
                stack.append((i, nums[i]))
       return False
    


class Solution(object):
    def canJump(self, nums):
        targetIndex = len(nums) - 1
        visited = len(nums) * [False]
        return self.dfs(nums, targetIndex, 0, visited)

    def dfs(self, nums, targetIndex, currentIndex, visited):
        if currentIndex == targetIndex:
            return True

        if visited[currentIndex]:
            return False
        visited[currentIndex] = True

        maxJumpLength = min(currentIndex + nums[currentIndex], len(nums) - 1)

        for nextIndex in range(currentIndex + 1, maxJumpLength + 1):
            if self.dfs(nums, targetIndex, nextIndex, visited):
                return True

        return False

nums = [3, 2, 1, 0, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution(object):
    def canJump(self, nums):
        memo = ['UNKNOWN'] * len(nums)
        memo[-1] = 'GOOD'
        return self.dfs(nums, len(nums) - 1, 0, memo)

    def dfs(self, nums, targetIndex, currentIndex, memo):
        if memo[currentIndex] != 'UNKNOWN':
            return memo[currentIndex] == 'GOOD'

        if currentIndex == targetIndex:
            memo[currentIndex] = 'GOOD'
            return True

        maxJumpLength = min(currentIndex + nums[currentIndex], len(nums) - 1)

        for nextIndex in range(currentIndex + 1, maxJumpLength + 1):
            if self.dfs(nums, targetIndex, nextIndex, memo):
                memo[currentIndex] = 'GOOD'
                return True

        memo[currentIndex] = 'BAD'
        return False
    
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution:
    def __init__(self):
        self.memo = []

    def canJumpFromPosition(self, position, nums):
        if self.memo[position] != 'UNKNOWN':
            return self.memo[position] == 'GOOD'

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(next_position, nums):
                self.memo[position] = 'GOOD'
                return True

        self.memo[position] = 'BAD'
        return False

    def canJump(self, nums):
        self.memo = ['UNKNOWN'] * len(nums)
        self.memo[-1] = 'GOOD'
        return self.canJumpFromPosition(0, nums)

    def __repr__(self):
        return f"Solution(memo={self.memo})"

nums = [3, 2, 0, 1, 2, 3]
print(Solution().canJump(nums))





class Solution(object):
    def canJump(self, nums):
        memo = ['UNKNOWN'] * len(nums)
        memo[-1] = 'GOOD'
        
        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == 'GOOD':
                    memo[i] = 'GOOD'
                    break
                    
        return memo[0] == 'GOOD'


class Solution(object):
    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0


class Solution(object):
    def canJumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True

        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                return True

        return False

    def canJump(self, nums):
        return self.canJumpFromPosition(0, nums)


nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution(object):
    def canJumpFromPosition(self, position, nums, visitCount):
        if position == len(nums) - 1:
            return True

        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            visitCount[nextPosition] += 1
            if self.canJumpFromPosition(nextPosition, nums, visitCount):
                return True

        return False

    def canJump(self, nums):
        visitCount = [0]*len(nums)
        return self.canJumpFromPosition(0, nums, visitCount), visitCount
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution(object):
    def canJump(self, nums):
        targetIndex = len(nums) - 1
        visited = [False]*len(nums)
        visitCount = [0]*len(nums)
        stack = [0]
        
        while stack:
            currentIndex = stack.pop()
            visitCount[currentIndex] += 1
            if currentIndex == targetIndex:
                return True
            if visited[currentIndex]:
                continue
            visited[currentIndex] = True
            furthestJump = min(currentIndex + nums[currentIndex], targetIndex)
            for nextIndex in range(currentIndex+1, furthestJump+1):
                if not visited[currentIndex]:
                    stack.append(nextIndex)
        
        return False, visitCount
nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))

class Solution(object):
    def canJumpFromPosition(self, position, nums, memo, visitCount):
        if memo[position] != self.Index.UNKNOWN:
            return True if memo[position] == self.Index.GOOD else False
        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position+1, furthestJump+1):
            visitCount[nextPosition] += 1
            if self.canJumpFromPosition(nextPosition, nums, memo, visitCount):
                memo[position] = self.Index.GOOD
                return True
        memo[position] = self.Index.BAD
        return False

    def canJump(self, nums):
        memo = [self.Index.UNKNOWN] * len(nums)
        memo[-1] = self.Index.GOOD
        visitCount = [0]*len(nums)
        return self.canJumpFromPosition(0, nums, memo, visitCount), visitCount

    class Index:
        GOOD, BAD, UNKNOWN = 1, 0, -1

nums = [3, 2, 1, 1, 4, 2, 1, 0, 1]
print(Solution().canJump(nums))