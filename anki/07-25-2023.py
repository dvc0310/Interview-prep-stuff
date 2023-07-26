import heapq

def find_taxi(n):
    heap = []
    for i in range(1, n):
        for j in range(i+1, n):  # We start from i+1 to avoid pairs (i, i)
            cube_sum = i**3 + j**3
            heapq.heappush(heap, (cube_sum, (min(i, j), max(i, j))))

    prev_sum = 0
    prev_pair = (0, 0)
    taxi = []
    count = 0  # Count the number of times the current cube sum has been found
    while heap:
        cube_sum, pair = heapq.heappop(heap)

        if cube_sum == prev_sum:
            count += 1
            if count == 2:  # The cube sum has been found with two different pairs
                taxi.append((cube_sum, prev_pair, pair))
        else:
            count = 1  # Reset the count for a new cube sum

        prev_sum = cube_sum
        prev_pair = pair

    return taxi


def triplets_smaller(nums, target):
    lst = []
    list.sort(nums)
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum < target:
                for k in range(r, l, -1):
                    lst.append((i, l, k))
                l += 1
            else:
                r -= 1
    return lst

nums = [-1, 4, 2, 1, 3]
target = 4

print(triplets_smaller(nums, target))

def bestTeamScoreRec(scores, ages):
    players = sorted(zip(scores, ages), key=lambda x: (x[1], x[0]))  # sort by age, then by score within the same age
    memo = {}  # memo[i] is the maximum score of a team that includes player i

    def dp(i):  # dp(i) is the maximum score of a team that includes player i and all previous players
        if i in memo:
            return memo[i]  # retrieve the result from memo if it's already computed
        max_score = players[i][0]  # initialize with the score of player i
        for j in range(i):
            if players[i][0] >= players[j][0]:  # no conflict
                max_score = max(max_score, dp(j) + players[i][0])  # include player j and all previous players
        memo[i] = max_score  # store the result in memo
        return max_score

    return max(dp(i) for i in range(len(players)))  # compute the maximum score for all teams



ages  = [1,1,2,2,2]
scores = [5,5,4,5,6]
print(bestTeamScoreRec(scores, ages))