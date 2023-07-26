class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][1] >= intervals[i-1][1] and \
                    intervals[i][0] < intervals[i-1][1] or intervals[i] == intervals[i-1]:
                intervals[i] = intervals[i-1]
                count += 1

        return count

intervals = [[1,3],[2,4],[5,7]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1,2],[3,4],[5,6],[7,8]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1,5],[2,6],[3,7],[4,8]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1,2]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1,100],[2,3],[4,5],[6,7],[8,9]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1,3],[2,4],[4,6],[5,7],[6,8]]
print(Solution().eraseOverlapIntervals(intervals))
intervals = [[1,3],[3,5],[5,7],[7,9]]
print(Solution().eraseOverlapIntervals(intervals))