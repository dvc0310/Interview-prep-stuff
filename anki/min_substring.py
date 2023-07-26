from collections import deque
def min_sub(s, t):
    letters = set(t)
    tracker = deque()
    tracker2 = deque()
    left = 0
    right = 1
    lst = []
    if s[left] in letters:
        tracker.append((s[left]))
        tracker2.append(left)
    while right < len(s):
        if s[right] in letters:
            if len(tracker) == 0:
                left = right
            tracker.append(s[right])
            tracker2.append(right)
        if letters.issubset(tracker):
            lst.append(s[left:right+1])
            tracker.popleft()
            tracker2.popleft()
            left = tracker2[0]
        right += 1
    return lst

def coins(n):
    left = 0
    right = n
    while left <= right:
        mid = (right + left) // 2
        k = mid * (mid + 1) // 2
        if k > n:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1

print(coins(8))

print(min_sub("abkcabc", "abc"))
