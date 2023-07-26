class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack1.pop()
    
    def enequeue(self, item):
        self.stack1.push(item)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

    def __repr__(self, level=0, prefix=""):
        ret = "    " * level + prefix + ":" + repr(self.endOfString) + "\n"
        for child in self.children:
            ret += self.children[child].__repr__(level+1, prefix+child)
        return ret

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for _, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfString = True

    def search(self, word):
        node = self.root
        for _, char in enumerate(word):
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfString
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def __repr__(self):
        return self.root.__repr__()
    
    def print(self):
        print(self.__repr__())
    
def main():
    # Initialize a Trie object
    trie = Trie()

    # Insert words
    words = ['apple', 'banana', 'grape', 'grapefruit', 'mango', 'kiwi']
    for word in words:
        trie.insert(word)
        trie.print()

    # Search for some words
    search_words = ['apple', 'grape', 'orange', 'grapefruit', 'kiwi']
    for word in search_words:
        if trie.search(word):
            print(f"The word '{word}' is in the trie")
        else:
            print(f"The word '{word}' is not in the trie")

    # Check if any words start with some prefixes
    prefixes = ['ap', 'gra', 'ki', 'ora', 'ban']
    for prefix in prefixes:
        if trie.startsWith(prefix):
            print(f"There's a word in the trie that starts with '{prefix}'")
        else:
            print(f"There's no word in the trie that starts with '{prefix}'")

if __name__ == "__main__":
    main()


def twosum(nums, target):
    hashmap = {}
    for num in nums:
        hashmap[num] = abs(target - num)
        if abs(target - num) in hashmap.keys():
            return [num, target - num]
    return [-1, -1]

def twoSum(nums, target):
    hashmap = {}
    for num in nums:
        complement = target - num
        if complement in hashmap:
            return [complement, num]
        hashmap[num] = num
    return [-1, -1]

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return [-1, -1]

nums = [1,2,3,4,7,8]
target = 10

print(twoSum(nums, target))
import copy
class Solution:
    def combo(self, k, n):
        self.lst = []
        currLst = []
        
        self.helper(k, n, currLst, 1, n, k)
        return self.lst
    
    def helper(self, k, n, currLst, idx, idx_end, c):
        if c == 0 and n == 0:
            self.lst.append(copy.deepcopy(currLst))
            currLst.pop()
            return
        if c == 0:
            currLst.pop()
            return
        for i in range(idx, idx_end):
            if i not in currLst:
                currLst.append(i)
                c -= 1
            self.helper(k, n - i, currLst, idx + 1, idx_end, c)
            c = k - len(currLst)
        if currLst:
            currLst.pop()
        return
    

import copy

class Solution:
    def combo(self, k, n):
        self.lst = []
        self.helper(k, n, [], 1)
        return self.lst
    
    def helper(self, k, n, currLst, idx):
        if len(currLst) == k and n == 0:
            self.lst.append(copy.deepcopy(currLst))
            return
        if len(currLst) == k or n < 0:
            return
        for i in range(idx, 10):  # As per the problem statement, numbers are between 1 and 9
            currLst.append(i)
            self.helper(k, n - i, currLst, i + 1)
            currLst.pop()  # undo the choice for the next iteration  


class Solution:
    def combinationSum3(self, k, n):
        result = []
        self.dfs(range(1,10), k, n, 0, [], result)
        return result
    
    def dfs(self, nums, k, n, index, path, result):
        # If no more numbers are needed and the sum is zero, add the path to result
        if k == 0 and n == 0:
            result.append(path)
            return 
        # If no more numbers are needed or the sum is zero, stop
        if k == 0 or n == 0:
            return 
        for i in range(index, len(nums)):
            # If the current number is greater than the sum, stop
            if nums[i] > n:
                break
            # Recurse with one fewer numbers needed and the sum reduced by the current number
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], result)

print(Solution().combinationSum3(3, 9))

def asteroids(input):
    stack = []
    for i in range(len(input)):
        if stack and input[i] < 0 and stack[-1] > 0:
            last = stack[-1]
            while stack and (input[i] < 0 and stack[-1] > 0) and -input[i] >= stack[-1]:
                last = stack.pop()
                if -last == input[i]:
                    break
        else:
            stack.append(input[i])


                
    return stack

input =  [1, 2, -2, 1, -2, -2, -5, -4]
asteroids(input)


def mergeIntervals(intervals):
    list.sort(intervals, key=lambda x: x[0])
    lst = [intervals[0]]
    for _, interval in enumerate(intervals[1:]):
        last = lst[-1]
        if last[1] >= interval[0]:
            last[1] = max(interval[1], last[1])
        else:
            lst.append(interval)
    return lst

intervals = [[1,3],[2,6],[8,10],[15,18]]
mergeIntervals(intervals)

def twoSum(nums, target):
    hashmap = {}
    for num in nums:
        complement = target - num
        if complement in hashmap:
            return [complement, num]
        hashmap[num] = num
    return [-1, -1]

def foursum(nums):

    return

nums = [1,0,-1,0,-2,2]
target = 0

class Solution:
    def hasCycle(self, matrix):
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if visited[row][col] == 0 and self.dfs(matrix, row, col, visited, None):
                    return True
        return False

    def dfs(self, matrix, row, col, visited, parent):
        stack = [(row, col, False, parent)]
        hasCycle = False
        while stack:
            y, x, backtrack, parent = stack.pop()
            if backtrack:
                visited[y][x] = 2
            else:
                if visited[y][x] == 0:
                    visited[y][x] = 1
                    stack.append((y, x, True, None))
                    for neighbor in self.neighbors(matrix, y, x):
                        if (neighbor[0], neighbor[1]) != parent:
                            stack.append((neighbor[0], neighbor[1], False, (y, x)))
                elif visited[y][x] == 1:
                    hasCycle = True
        return hasCycle

    def neighbors(self, matrix, row, col):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == matrix[row][col]:
                yield new_row, new_col

matrix = [["a", "b", "e", "b"],
          ["b", "b", "b", "b"],
          ["b", "c", "c", "d"],
          ["c", "c", "d", "d"]]
print(Solution().hasCycle(matrix))

