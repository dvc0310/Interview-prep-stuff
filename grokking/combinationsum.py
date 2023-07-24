class Solution(object):
  def combinationSum(self, candidates, target):
    res = []  # To store the final result
    self.backtrack(candidates, 0, target, [], res)
    return res

  def backtrack(self, candidates, start, target, comb, res):
    # If target is 0, we have found a valid combination
    if target == 0:
      # Append a copy of the current combination to the result list
      res.append(list(comb))
      return
    # Iterate through the candidates array starting from the given index
    for i in range(start, len(candidates)):
      # If the current candidate is greater than the remaining target, move on to the next
      if target < candidates[i]:
        continue
      # Add the current candidate to the current combination
      comb.append(candidates[i])
      # Recursively call the function with the updated combination and remaining target
      self.backtrack(candidates, i, target - candidates[i], comb, res)
      # Backtrack by removing the last added candidate from the combination
      comb.pop()


def main():
  # Test case 1
  candidates = [2, 3, 6, 7]
  target = 7
  s = Solution()
  print(s.combinationSum(candidates, target))  # expected output: [[2, 2, 3], [7]]

  # Test case 2
  candidates = [2, 3, 5]
  target = 8
  s = Solution()
  print(
      s.combinationSum(candidates, target)
  )  # expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

  # Test case 3
  candidates = []
  target = 8
  s = Solution()
  print(s.combinationSum(candidates, target))  # expected output: []

  # Test case 4
  candidates = [5, 10, 15]
  target = 20
  s = Solution()
  print(
      s.combinationSum(candidates, target)
  )  # expected output: [[5,5,5,5], [5,5,10], [5,15], [10,10]]

  # Test case 5
  candidates = [2, 4, 6, 8]
  target = 10
  s = Solution()
  print(
      s.combinationSum(candidates, target)
  )  # expected output: [[2,2,2,2,2], [2,2,2,4], [2,2,6], [2,4,4], [2,8], [4,6]]

  # Test case 6
  candidates = [2, 3, 5]
  target = 0
  s = Solution()
  print(s.combinationSum(candidates, target))  # expected output: [[]]


main()
