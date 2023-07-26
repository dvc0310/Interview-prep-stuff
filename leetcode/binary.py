class Solution:
  def search(self, arr, key):
    l = 0
    r = len(arr) - 1
    if arr[l] > arr[r]:
        while l <= r:
            m = l + (r - l) // 2
            if key == arr[m]:
                return m
            if arr[m] < key:
                r = m - 1
            else:
                l = m + 1
            
    else:
        while l <= r:
            m = (l + r) // 2
            if key == arr[m]:
                return m
            if arr[m] > key:
                r = m - 1
            elif arr[m] < key:
                l = m + 1
    return -1 

arr = [10, 6, 4]
key = 10
Solution().search(arr, key)

class Solution:
  def searchCeilingOfANumber(self, arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if key == arr[m]:
            return m
        if arr[m] > key:
            r = m - 1
        elif arr[m] < key:
            l = m + 1
    if l > len(arr) - 1:
        return -1
    return l

arr =  [4,6,10]
key = 17
print(Solution().searchCeilingOfANumber(arr, key))

class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[0] if left == len(letters) else letters[left]



class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

Solution().search([-1,0,3,5,9,12], 9)