def taxi(n):

    lst = []
    for i in range(1, n):
        for j in range(i, n):
            lst.append((i**3 + j**3, min(i, j), max(i,j)))

    lst = sorted(list(set(lst)), key=lambda x: x[0])
    taxi = []
    for i in range(1, len(lst)):
        if lst[i][0] == lst[i-1][0]:
            taxi.append(lst[i][0])
    
    return list(set(taxi))

taxi(30)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def find_LCA(root, node1, node2):
    if root is None:
        return None
    if root.value == node1 or root.value == node2:
        return root

    left_lca = find_LCA(root.left, node1, node2)
    right_lca = find_LCA(root.right, node1, node2)

    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca

    else:
        return right_lca

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("The first common ancestor is ", find_LCA(root, 4, 5).value)


from collections import defaultdict

def min_substring(s, t):
    freq_t = defaultdict(int)
    for char in t:
        freq_t[char] += 1

    counter = len(freq_t)

    left, right = 0, 0

    min_length = float('inf')
    min_str = ""

    while right < len(s):
        if s[right] in freq_t:
            freq_t[s[right]] -= 1
            if freq_t[s[right]] == 0:
                counter -= 1

        right += 1
        while counter == 0:
            if right - left < min_length:
                min_length = right - left
                min_str = s[left:right]

            if s[left] in freq_t:
                freq_t[s[left]] += 1
                if freq_t[s[left]] > 0:
                    counter += 1

            left += 1

    return min_str if min_length != float('inf') else ""


# Test
s = "ADOBECODEBANC"
t = "ABC"
print(min_substring(s, t))  # Output: BANC

class Solution(object):
    def uniqueOccurrences(self, arr):
        hashmap = {}
        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                
        return len(hashmap.values()) == len(set(hashmap.values()))

print(Solution().uniqueOccurrences([26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]))