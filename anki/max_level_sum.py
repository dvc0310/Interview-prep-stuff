from treeclass import TreeNode
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        lst = []
        
        while queue:
            level_length = len(queue)
            sum = 0
            for _ in range(level_length):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lst.append(sum)
            sum = 0
            
        return lst.index(max(lst))+ 1
  

    def find_zigzag(self, root):
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


root1 = TreeNode().create_tree([3,5,1,6,2,9,8,None,None,7,4])
root2 = TreeNode().create_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
root = TreeNode().create_tree([1,None,2,3,4,None,None,5,6,None,7,None,None,None,8])
print(Solution().find_zigzag(root))
