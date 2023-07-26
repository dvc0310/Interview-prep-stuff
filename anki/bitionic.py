def bitonic_search(arr, num):
    # Find the peak
    peak = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak = i
        else:
            break

    # Binary search on increasing part
    ls, le = 0, peak
    while ls <= le:
        lm = (ls + le) // 2
        if num == arr[lm]:
            return True
        elif num < arr[lm]:
            le = lm - 1
        else:
            ls = lm + 1

    # Binary search on decreasing part
    rs, re = peak + 1, len(arr) - 1
    while rs <= re:
        rm = (rs + re) // 2
        if num == arr[rm]:
            return True
        elif num < arr[rm]:
            rs = rm + 1
        else:
            re = rm - 1
    
    return False

# Example usage
bitonic_array = [1, 5, 7, 9, 11, 15, 20, 18, 14, 11, 8, 6, 2]
print(bitonic_search(bitonic_array, 7))  # Should print True
print(bitonic_search(bitonic_array, 22))  # Should print False


