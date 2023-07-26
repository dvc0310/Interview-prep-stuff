import heapq
def kthLargest(nums, k):
    heap = []
    for number in nums:
        heapq.heappush(heap, -number)
    num = -99999
    while k > 0:
        num = -heapq.heappop(heap)
        k -= 1
    return  num

nums = [3,2,1,5,6,4]
k = 2
print(kthLargest(nums, k))

matrix = [["1","1","1","1","1"],
          ["1","1","0","1","1"],
          ["1","1","1","1","1"],
          ["1","1","1","1","1"],
          ["1","1","1","1","1"],
          ["1","1","1","1","0"]]

def maximalSquare(matrix):
    rowLength = len(matrix)
    colLength = len(matrix[0])
    dp = [[0]*(colLength+1) for _ in range(rowLength+1)]
    max_side = 0
    for row in range(rowLength):
        for col in range(colLength):
            if matrix[row][col] == '1':
                dp[row+1][col+1] = min(dp[row][col], dp[row][col+1], dp[row][col+1]) + 1 
                max_side = max(max_side, dp[row+1][col+1])
    
    
    return max_side ** 2

print(maximalSquare(matrix))