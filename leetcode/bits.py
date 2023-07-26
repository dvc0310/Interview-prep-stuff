def bitCount(n):
    lst = []
    for i in range(n+1):
        lst.append(bitCountHelper(i))
    return lst
        
def bitCountHelper(n):
    count = 0
    while n > 0:
        count += n%2
        n = n // 2
    
    return count

def bitcountDP(n):
    dp = [0,1,1,2]
    if n < 5:
        return dp[:n+1]
    dp.extend([0]*(n-3))
    offshoot = 1
    for i in range(4, n+1):
        if i & (i - 1) == 0:
            offshoot += 1
        dp[i] = dp[i - 2**offshoot] + 1
    return dp

print(bitcountDP(30))
print(bitCount(30))
    
    