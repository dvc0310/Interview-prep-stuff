import random

def kadane(arr):
    max_so_far = 0
    current_max = 0
    for i in range(0, len(arr)):
        current_max += arr[i]
        if max_so_far < current_max:
            max_so_far = current_max
        if current_max < arr[i]:
            current_max = arr[i]
    return max_so_far

def kadane2(arr):
    max_so_far = 0
    current_max = 0
    start = 0
    end = 0
    for i in range(0, len(arr)):
        current_max += arr[i]
        if max_so_far < current_max:
            max_so_far = current_max
            end = i
        if current_max < arr[i]:
            current_max = arr[i]
            start = i
    return arr[start:end+1]

def main():
    #A = [10, 10, 1, -6, 7, 2, 10, -10, -3, -5]
    A = []
    for i in range (0 ,10):
         A.append (random.randint(-10, 10))
    
    print (A)
    max_sum = kadane(A)
    max_arr = kadane2(A)
    print("Maximum contiguous sum is ", max_sum)
    print("Maximum contiguous array is ", max_arr)

if __name__ == "__main__":
    main()
