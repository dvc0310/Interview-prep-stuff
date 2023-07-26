import random


def max_crossing_sum(arr, low, mid, high):
    curr_left_sum = 0
    max_left_sum = float('-inf')
    for i in range(mid, low - 1, -1):
        curr_left_sum = curr_left_sum + arr[i]
        if max_left_sum < curr_left_sum:
            max_left_sum = curr_left_sum
    
    curr_right_sum = 0
    max_right_sum = float('-inf')
    for i in range(mid + 1, high + 1):
        curr_right_sum = curr_right_sum + arr[i]
        if max_right_sum < curr_right_sum:
            max_right_sum = curr_right_sum
        
        
    return max(max_left_sum + max_right_sum, max_left_sum, max_right_sum)
    
def max_contiguous_sum(arr, low, high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    left_sum = max_contiguous_sum(arr, low, mid)
    right_sum = max_contiguous_sum(arr, mid+1, high)
    cross = max_crossing_sum(arr, low, mid, high)
    
    return max(cross, left_sum, right_sum)

def main():
    A = [10, 10, 1, -6, 7, 2, 10, -10, -3, -5]
    # for i in range (0 ,10):
    #     A.append (random.randint(-10, 10))
    
    print (A)
    max_sum = max_contiguous_sum(A, 0, len(A) - 1)
    print("Maximum contiguous sum is ", max_sum)

if __name__ == "__main__":
    main()
