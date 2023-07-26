class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        c = intervals[1:]

        for current_interval in c:
            last_merged_interval = merged[-1]

            if current_interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
            else:
                merged.append(current_interval)
        return merged

