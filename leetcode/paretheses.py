class Solution(object):
    def generateParenthesis(self, n):
        # Initialize a list of empty lists for dp where dp[i] will store 
        # all valid parentheses strings of length i
        dp = [[] for _ in range(n + 1)]
        
        # The base case is an empty string
        dp[0] = ['']

        # For each parentheses string length from 1 to n
        for length in range(1, n + 1):
            # For each possible partition of the string length
            for partition in range(length):
                # For every combination of the left partition (inner)
                for left in dp[partition]:
                    # For every combination of the right partition (outer)
                    for right in dp[length - partition - 1]:
                        # Add a new combination to the list for this length
                        dp[length].append('(' + left + ')' + right)
                        
            # Removing duplicates
            dp[length] = list(set(dp[length]))

        # Return the list of all valid combinations of length n
        return dp[n]

    
    def generateParenthesis2(self, n):
        dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
    
    def generateParenthesis4(n):
        dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(1, n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        dp[i].append('(' + x + ')' + y)
        return dp[n]

def generateParenthesis(n):
    memo = {0: ['']}
    return generate(n, memo)

def generate(n, memo):
    if n not in memo:
        result = []
        for i in range(n):
            for left in generate(i, memo):
                for right in generate(n - 1 - i, memo):
                    result.append('({}){}'.format(left, right))
        memo[n] = result
    return memo[n]

from collections import deque

def generateParenthesis(n):
    res = []
    stack = [("(", 1, 0)]  # initialize the stack with an open parenthesis, count of open and close parentheses
    while stack:
        parenthesis, open_count, close_count = stack.pop()
        if open_count == close_count == n:  # if the parenthesis string is valid
            res.append(parenthesis)
        if open_count < n:  # add more open parentheses
            stack.append((parenthesis + "(", open_count + 1, close_count))
        if close_count < open_count:  # add more close parentheses
            stack.append((parenthesis + ")", open_count, close_count + 1))
    return res



print(generateParenthesis(3))  # should return ['()']


from collections import deque

def generateParenthesis(n):
    # Tuple contains the string, number of open parentheses, number of closed parentheses
    queue = deque([("", 0, 0)])
    result = []

    while queue:
        s, open_p, close_p = queue.popleft()

        # If we've used all parentheses and the string is valid, append to the result
        if open_p == close_p == n:
            result.append(s)

        # If we still have some open parentheses left, add to the string and queue
        if open_p < n:
            queue.append((s + "(", open_p + 1, close_p))

        # If we have less closed parentheses than open, add to the string and queue
        if close_p < open_p:
            queue.append((s + ")", open_p, close_p + 1))

    return result

print(Solution().generateParenthesis2(3))  # should return ['((()))', '(()())', '(())()', '()(())', '()()()']
print(generateParenthesis(1))  # should return ['()']


