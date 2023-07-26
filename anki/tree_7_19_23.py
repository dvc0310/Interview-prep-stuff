from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_tree(self, levelorder):
        if not levelorder:
            return None
        root_value = levelorder.pop(0)
        root = TreeNode(root_value) if root_value is not None else None
        queue = deque([root])

        while levelorder:
            current_node = queue.popleft()

            # for each node we will have two children in level order list
            left_value = levelorder.pop(0)
            if left_value is not None:
                left_node = TreeNode(left_value)
                current_node.left = left_node
                queue.append(left_node)

            if levelorder:  # if there is still values left
                right_value = levelorder.pop(0)
                if right_value is not None:
                    right_node = TreeNode(right_value)
                    current_node.right = right_node
                    queue.append(right_node)

        return root
        
    def __repr__(self, level=0):
        ret = "\t"*level + repr(self.val) + "\n"
        if self.left:
            ret += self.left.__repr__(level + 1)
        if self.right:
            ret += self.right.__repr__(level + 1)
        return ret

def build_tree(nodes, i, n):
    root = None
    if (i < n) and nodes[i] is not None:
        root = TreeNode(nodes[i])
        root.left = build_tree(nodes, 2*i + 1, n)
        root.right = build_tree(nodes, 2*i + 2, n)
    return root

# Recursive solution
class SolutionRecursive:
    def longestZigZag(self, root):
        self.max_length = 0
        self.dfs(root)
        return self.max_length

    def dfs(self, node):
        if node is None:
            return [-1, -1]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.max_length = max(self.max_length, left[1] + 1, right[0] + 1)

        return [left[1] + 1, right[0] + 1]

# Iterative solution 1
class SolutionIterative1:
    def longestZigZag(self, root):
        stack = [(root, False, 0)]
        max_length = 0

        while stack:
            node, is_left, length = stack.pop()
            max_length = max(max_length, length)
            
            if node.left:
                stack.append((node.left, False, length + 1 if is_left else 1))
            if node.right:
                stack.append((node.right, True, length + 1 if not is_left else 1))

        return max_length

# Iterative solution 2
class SolutionIterative2:
    def longestZigZag(self, root):
        stack = [(root, 's', 0)]
        maxsum = 0
        while stack:
            node, dir, sum= stack.pop()
            lsum = sum
            rsum = sum
            if node:
                if node.right:
                    if dir == 's' or dir == 'l':
                        rsum = sum + 1
                    else: 
                        rsum = 1
                    newDir = 'r'
                    stack.append((node.right, newDir, rsum))
                if node.left:
                    if dir == 's' or dir == 'r':
                        lsum = sum + 1
                    else: 
                        lsum = 1
                    newDir = 'l'
                    stack.append((node.left, newDir, lsum))
            maxsum = max(maxsum, lsum, rsum, sum)
        return maxsum
    
class Solution:
    def find_path_sum(self, root, target):
        self.cache = {0: 1} 
        self.count = 0
        self.helper(root, target, 0)
        return self.count
    def helper(self, root, target, sum):
        if root == None:
            return
        
        sum += root.val

        self.count += self.cache.get(sum - target, 0)
        self.cache[sum] = self.cache.get(sum, 0) + 1

        self.helper(root.left, target, sum)
        self.helper(root.right, target, sum)

        if self.cache[sum] == 1:
            del self.cache[sum]  # Completely remove from cache if count becomes 0
        else:
            self.cache[sum] -= 1


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = build_tree(nodes, 0, len(nodes))
    
    recursive_solution = SolutionRecursive().longestZigZag(root)
    iterative_solution_1 = SolutionIterative1().longestZigZag(root)
    iterative_solution_2 = SolutionIterative2().longestZigZag(root)

    print(f"Recursive Solution: {recursive_solution}")
    print(f"Iterative Solution 1: {iterative_solution_1}")
    print(f"Iterative Solution 2: {iterative_solution_2}")
    root = TreeNode().create_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    targetSum = 8
    print(Solution().find_path_sum(root, 8))
