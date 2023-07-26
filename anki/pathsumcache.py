# First, let's define the TreeNode structure for testing

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"

# Now let's build a binary tree for testing

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

target_sum = 8

# Now, let's convert the recursive solution to an iterative one

class Solution:
    def find_path_sum_rec(self, root, target):
        # key: prefix sum, value: frequency of the prefix sum
        self.cache = {0: 1}
        self.count = 0
        self.target = target

        self.dfs(root, 0)
        return self.count

    def dfs_rec(self, node, curr_path_sum):
        if not node:
            return 

        # compute prefix sum
        curr_path_sum += node.val

        # check if there is a subarray sum equals to the target
        old_path_sum = curr_path_sum - self.target
        self.count += self.cache.get(old_path_sum, 0)

        # update the prefix sum frequency
        self.cache[curr_path_sum] = self.cache.get(curr_path_sum, 0) + 1

        # dfs break down 
        self.dfs_rec(node.left, curr_path_sum)
        self.dfs_rec(node.right, curr_path_sum)

        # when move to a different branch, the prefix sum is no longer available, hence remove it
        self.cache[curr_path_sum] -= 1

    def find_path_sum_iter2(self, root, target):
        # key: prefix sum, value: frequency of the prefix sum
        cache = {0: 1}
        count = 0

        # stack for DFS, storing (node, parent path sum)
        stack = [(root, 0)]

        while stack:
            node, curr_path_sum = stack.pop()

            if node:
                curr_path_sum += node.val

                old_path_sum = curr_path_sum - target
                count += cache.get(old_path_sum, 0)

                cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

                stack.append((node.right, curr_path_sum))
                stack.append((node.left, curr_path_sum))

        return count

    def find_path_sum_iter(self, root, target):
        cache = {0: 1}
        count = 0

        stack = [(root, 0, False)]

        while stack:
            node, curr_path_sum, visited = stack.pop()

            if node:
                if not visited:
                    curr_path_sum += node.val

                    old_path_sum = curr_path_sum - target
                    count += cache.get(old_path_sum, 0)

                    cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

                    stack.append((node, curr_path_sum, True))  
                    stack.append((node.right, curr_path_sum, False))
                    stack.append((node.left, curr_path_sum, False))
                else:
                    cache[curr_path_sum] -= 1  # subtract from the cache when leaving a node

        return count




Solution().find_path_sum_iter(root, target_sum)


