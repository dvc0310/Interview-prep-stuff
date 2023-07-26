def mincost(cost):
    dp = len(cost) * [0]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
    return dp[-1]

cost = [1,100,1,1,1,100,1,1,100,1]
mincost(cost)

def gcd(a, b):
    while a % b > 0:
        a, b = b, a % b
    return b

def stringDivides(s1, s2):
    gcd_int = gcd(len(s1), len(s2))
    gcd_s1 = s1[:gcd_int]
    gcd_s2 = s2[:gcd_int]
    if gcd_s1 == gcd_s2 and s1 == gcd_s1 * (len(s1) // len(gcd_s1)) and s2 == gcd_s2 * (len(s2) // len(gcd_s2)):
        return gcd_s1 
    return ''