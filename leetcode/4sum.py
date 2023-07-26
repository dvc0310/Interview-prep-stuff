def four_sum(arr, target):
    n = len(arr)

    if n < 4:
        return []

    sums = dict()
    results = []
    
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]

            remaining = target - current_sum
            if remaining in sums:
                for pair in sums[remaining]:
                    if i not in pair and j not in pair:  # check if pairs are disjoint
                        quad = [arr[pair[0]], arr[pair[1]], arr[i], arr[j]]
                        quad.sort()  # sort to handle duplicates
                        if quad not in results:
                            results.append(quad)
            
            if current_sum not in sums:
                sums[current_sum] = [(i, j)]
            else:
                sums[current_sum].append((i, j))

    return results

nums = [1,0,-1,0,-2,2]
target = 0
four_sum(nums, target)
