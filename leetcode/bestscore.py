def bestTeamScore(scores, ages):
    players = sorted(zip(scores, ages), key=lambda x: (x[1], x[0]))  # sort by age, then by score within the same age
    dp = [0] * len(players)  # dp[i] is the maximum score of a team that includes player i
    for i in range(len(players)):
        dp[i] = players[i][0]  # initialize with the score of player i
        for j in range(i):
            if players[i][0] >= players[j][0]:  # no conflict
                dp[i] = max(dp[i], dp[j] + players[i][0])
    return max(dp)


ages  = [1,1,2,2,2]
scores = [5,5,4,5,6]
print(bestTeamScore(scores, ages))
