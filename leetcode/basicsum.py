class Solution:
  def calculate_sum(self, N):
    # TODO: Write your code here
    if N <= 0:
        return 0
    else:
        return N + self.calculate_sum(N-1)

print(Solution().calculate_sum(5))

class Solution:
  def calculate_factorial(self, number):
    # TODO: Write your code here
    if number == 1:
        return 1
    else:
        return number * self.calculate_factorial(number - 1)

print(Solution().calculate_factorial(7))

class Solution:
  def calculate_gcd(self, A, B):
    if A > B:
        A, B = B, A
    
    return self.helper(A, B)

  def helper(self, A, B):
      if B % A == 0:
          return A
      
      return self.helper(B % A, A)

print(Solution().calculate_gcd(40, 60))

class Solution:
  def fibonacci(self, number):
    self.cache = [-1] * (number + 1)
    self.cache[0] = 0
    self.cache[1] = 1
    return self.fib(number)
    
  def fib(self, number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    else:
        if self.cache[number] != -1:
            return self.cache[number]
        left = self.fib(number - 1) 
        right = self.fib(number - 2)
        self.cache[number] = left + right
        return left + right
    
print(Solution().fibonacci(10))

class Solution:
    def __init__(self):
        self.cache = {}

    def Ackermann(self, m, n):
        if (m, n) in self.cache:
            return self.cache[(m, n)]
        
        if m == 0:
            result = n + 1
        elif m > 0 and n == 0:
            result = self.Ackermann(m - 1, 1)
        else:
            result = self.Ackermann(m - 1, self.Ackermann(m, n - 1))

        self.cache[(m, n)] = result
        return result


print(Solution().Ackermann(3,2))