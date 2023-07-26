from treeclass import TreeNode
from collections import deque
import copy


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        
    def rightSideView(self, root):
        if not root:
            return []
        
        queue = deque([root])
        right_side_view = []
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    right_side_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return right_side_view
    
    def goodNodes(self, root):
        if not root:
            return 0

        stack = [(root, root.val)]
        count = 0
        while stack:
            node, max_val = stack.pop() 
            if node.val >= max_val:
                count += 1
                max_val = node.val

            if node.right:
                stack.append((node.right, max_val))
            if node.left:
                stack.append((node.left, max_val))

        return count
    

    def find_path(self, root, value):
        stack = [(root, [root])]
        while stack:
            (node, path) = stack.pop()
            if node and node.val == value:
                return path
            if node:
                if node.right:
                    stack.append((node.right, path + [node.right]))
                if node.left:
                    stack.append((node.left, path + [node.left]))
        return None
    

    def leafSimilar(self, root1, root2):
        return set(self.similar(root1)) == set(self.similar(root2))

    def similar(self, root):
        if not root:
            return []
        
        queue = [root]
        lst = []
        
        while queue:
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.pop()
                if not node.left and not node.right:
                    lst.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return lst

    def find_path_sum(self, root, target):
        lst = deque()
        lst.append(root.val)
        stack = [(root, root.val, lst)]
        paths = []
        while stack:
            (node, path_sum, queue) = stack.pop()
            if node:
                if node.right:
                    right_path_sum = path_sum + node.right.val
                    right_queue = copy.deepcopy(queue)   
                    right_queue.append(node.right.val)               
                    while right_path_sum > target:
                        right_path_sum -= right_queue.popleft()
                    if right_path_sum == target:
                        paths.append(list(right_queue))
                    stack.append((node.right, right_path_sum, right_queue))
                if node.left:
                    left_path_sum = node.left.val + path_sum
                    left_queue = copy.deepcopy(queue)   
                    left_queue.append(node.left.val)  
                    while left_path_sum > target:
                        left_path_sum -= left_queue.popleft()
                    if left_path_sum == target:
                        paths.append(list(left_queue))
                    stack.append((node.left,  left_path_sum, left_queue))
        return paths
    

class Solution2:
    def find_path_sum(self, root, target):
        # key: prefix sum, value: frequency of the prefix sum
        self.cache = {0: 1}
        self.count = 0
        self.target = target

        self.dfs(root, 0)
        return self.count

    def dfs(self, node, curr_path_sum):
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
        self.dfs(node.left, curr_path_sum)
        self.dfs(node.right, curr_path_sum)

        # when move to a different branch, the prefix sum is no longer available, hence remove it
        self.cache[curr_path_sum] -= 1

    def lowestCommonAncestor(self, root, p, q):
        path_p = self.findPathHelper(root, p.val)
        path_q = self.findPathHelper(root, q.val)
        common_elements = [x for x in path_p if x in path_q and path_p.index(x) == path_q.index(x)]
        
        return common_elements[-1]
    
    def findPathHelper(self, root, target):
        path = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if path and path[-1] == target:
                return path
            if visited:
                path.pop()
            else:
                stack.append((node, True))
                path.append(node.val)
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
                
        return path
    





    
root1 = TreeNode().create_tree([3,5,1,6,2,9,8,None,None,7,4])
root2 = TreeNode().create_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])

print(Solution().similar(root1))
print(Solution().similar(root2))
print(Solution().leafSimilar(root1, root2))

root = TreeNode().create_tree([3,1,4,3,None,1,5])
print(Solution().goodNodes(root1))
print(Solution().find_path(root1, 4))
root = TreeNode().create_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
targetSum = 8
print(Solution().find_path_sum(root, 8))
root = [3,5,1,6,2,0,8,None,None,7,4]
root = TreeNode().create_tree(root)

