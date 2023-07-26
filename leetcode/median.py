import heapq

# Create a heap
h = []
heapq.heapify(h)
print("Empty Heap:", h)  # []

# Insert elements into heap
heapq.heappush(h, 21)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 10)
print("Heap after insertion:", h)  # [1, 10, 3, 21]

# Remove and return smallest element from heap
print("Pop smallest element:", heapq.heappop(h))  # 1
print("Heap after pop:", h)  # [3, 10, 21]

# Push and pop elements from heap in one statement
print("Push and pop in one:", heapq.heappushpop(h, 15))  # 2
print("Heap after pushpop:", h)  # [3, 10, 21]

# Pop and push elements from heap in one statement
print("Pop and push in one:", heapq.heapreplace(h, 2))  # 3
print("Heap after replace:", h)  # [2, 10, 21]

# Transform list x into a heap
x = [10, 15, 30, 11, 20, 9, 21,]
heapq.heapify(x)
print("Heapify list:", x)  # [10, 20, 30, 40, 50]

# Get the 3 smallest items in the heap
print("Three smallest items:", heapq.nsmallest(3, x))  # [10, 20, 30]

# Get the 2 largest items in the heap
print("Two largest items:", heapq.nlargest(2, x))  # [50, 40]
