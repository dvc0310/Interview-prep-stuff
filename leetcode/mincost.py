class Solution():
    def minCostClimbingStairs(self, cost):
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        min_cost = [0] * len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min(min_cost[i-1], min_cost[i-2])

        return min(min_cost[-1], min_cost[-2])




