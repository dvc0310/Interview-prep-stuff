def arrange_coins(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        x = mid * (mid + 1) // 2
        if x <= n:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

arrange_coins(8)
