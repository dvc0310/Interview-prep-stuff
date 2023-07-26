def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]] 

    for current_interval in intervals[1:]:
        if current_interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current_interval[1])
        else:
            merged.append(current_interval)
            
    return merged

