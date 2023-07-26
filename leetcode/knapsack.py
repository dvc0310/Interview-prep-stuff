class Solution:
  def solve_knapsack(self, profits, weights, capacity):
    n = len(profits)
    # Create a stack and push the initial state
    stack = [(capacity, 0, 0)]  # capacity, currentIndex, profit
    max_profit = 0

    while stack:
      # Pop a state from the stack
      capacity, currentIndex, profit = stack.pop()

      # Base case: update max_profit
      if capacity <= 0 or currentIndex >= n:
        max_profit = max(max_profit, profit)
      else:
        # Exclude the item at currentIndex
        stack.append((capacity, currentIndex + 1, profit))
        
        # Include the item at currentIndex, if it does not exceed the capacity
        if weights[currentIndex] <= capacity:
          stack.append((capacity - weights[currentIndex], currentIndex + 1, profit + profits[currentIndex]))

    return max_profit

class Solution:
    def solve_knapsack(self, profits, weights, capacity):
        # Initialize memoization table with -1 for unsolved subproblems
        memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]

        # Stack to simulate recursion
        stack = [(0, capacity)]

        while stack:
            i, w = stack[-1]

            # If this subproblem has already been solved, pop it from the stack
            if memo[i][w] != -1:
                stack.pop()
                continue

            # If we've considered all items or used up all capacity, this subproblem is solved
            if i == len(profits) or w == 0:
                stack.pop()
                memo[i][w] = 0
                continue

            # Otherwise, consider two cases: including item i or excluding it
            if weights[i] <= w:
                # If we haven't solved the subproblem for including item i, add it to the stack
                if memo[i + 1][w - weights[i]] == -1:
                    stack.append((i + 1, w - weights[i]))
                # If we haven't solved the subproblem for excluding item i, add it to the stack
                if memo[i + 1][w] == -1:
                    stack.append((i + 1, w))
                # If both subproblems are solved, we can solve this one
                if memo[i + 1][w - weights[i]] != -1 and memo[i + 1][w] != -1:
                    memo[i][w] = max(profits[i] + memo[i + 1][w - weights[i]], memo[i + 1][w])
                    stack.pop()
            else:
                # If item i can't be included because it's too heavy, the solution is to exclude it
                # If we haven't solved the subproblem for excluding item i, add it to the stack
                if memo[i + 1][w] == -1:
                    stack.append((i + 1, w))
                # If the subproblem is solved, we can solve this one
                if memo[i + 1][w] != -1:
                    memo[i][w] = memo[i + 1][w]
                    stack.pop()

        # The solution to the original problem is in memo[0][capacity]
        return memo[0][capacity]


class Solution:
    def solve_knapsack(self, profits, weights, capacity):
        # Initialize memoization table with -1 for unsolved subproblems
        memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]

        # Stack to simulate recursion
        # Each state is a tuple of (index, remaining capacity)
        stack = [(0, capacity)]

        while stack:
            i, w = stack[-1]

            # If this subproblem has already been solved, pop it from the stack
            if memo[i][w] != -1:
                print(f"Memoized item {i} with remaining capacity {w} and current profit {memo[i][w]}")
                stack.pop()
                continue

            # If we've considered all items or used up all capacity, this subproblem is solved
            if i == len(profits) or w == 0:
                stack.pop()
                memo[i][w] = 0
                continue

            # Otherwise, consider two cases: including item i or excluding it
            if weights[i] <= w:
                # If we haven't solved the subproblem for including item i, add it to the stack
                if memo[i + 1][w - weights[i]] == -1:
                    stack.append((i + 1, w - weights[i]))
                # If we haven't solved the subproblem for excluding item i, add it to the stack
                if memo[i + 1][w] == -1:
                    stack.append((i + 1, w))
                # If both subproblems are solved, we can solve this one
                if memo[i + 1][w - weights[i]] != -1 and memo[i + 1][w] != -1:
                    memo[i][w] = max(profits[i] + memo[i + 1][w - weights[i]], memo[i + 1][w])
                    stack.pop()
            else:
                # If item i can't be included because it's too heavy, the solution is to exclude it
                # If we haven't solved the subproblem for excluding item i, add it to the stack
                if memo[i + 1][w] == -1:
                    stack.append((i + 1, w))
                # If the subproblem is solved, we can solve this one
                if memo[i + 1][w] != -1:
                    memo[i][w] = memo[i + 1][w]
                    stack.pop()

        # The solution to the original problem is in memo[0][capacity]
        return memo[0][capacity]

# Initialize the solution class
solver = Solution()

# Test the function
profits = [10, 15, 40]
weights = [1, 2, 3]
capacity = 4

print(solver.solve_knapsack(profits, weights, capacity))



