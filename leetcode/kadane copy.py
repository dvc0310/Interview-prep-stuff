def max_contiguous_sum(A):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, len(A)): 
        if A[i] < max_ending_here + A[i]:
            max_ending_here = max_ending_here + A[i]
        else:
            max_ending_here = A[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            
    return max_so_far

def max_sum(arr, k):
  window_sum = 0
  max_sum = 0

  for i in range(k):
    window_sum += arr[i]

  max_sum = window_sum

  for i in range(k, len(arr)):
    x = arr[i-k]
    y = arr[i]
    window_sum = window_sum - x + y

    max_sum = max(max_sum, window_sum)

  return max_sum

