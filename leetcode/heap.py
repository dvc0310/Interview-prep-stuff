import random
import heapq
import statistics
def heapify_min(arr, arr_size, root_index):
    smallest_index = root_index 
    left_index = 2 * root_index + 1 
    right_index = 2 * root_index + 2 
    
    if left_index < arr_size and arr[root_index] > arr[left_index]:
        smallest_index = left_index
    
    if right_index < arr_size and arr[smallest_index] > arr[right_index]:
        smallest_index = right_index
    
    if smallest_index != root_index:
        arr[root_index], arr[smallest_index] = arr[smallest_index], arr[root_index] # swap
        heapify_min(arr, arr_size, smallest_index)
 
def build_min_heap(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)

def insert(A, element):
    A.append(element)
    build_min_heap(A)

def remove_median(A):
    sorted = []
    while len(A) != 0: # loop n times
        sorted.append(heapq.heappop(A)) # O(log n) time per pop
    median_index = len(sorted)//2
    if len(sorted) % 2 == 0:
        median_index = len(sorted)//2 - 1
    median = sorted.pop(median_index)
    A = sorted
    build_min_heap(A)
    return median

A = []
for i in range (0 ,10):
        A.append (random.randint(-10, 10))
    
    
build_min_heap(A)
print(A)
insert(A, 83)
print(A)
print(statistics.median(A))
print(remove_median(A))
print(A)
print(statistics.median(A))
print(remove_median(A))
print(A)