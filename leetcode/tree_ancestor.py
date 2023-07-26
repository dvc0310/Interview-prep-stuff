class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"
        
    def create_tree(self, lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        front = 0
        index = 1
        while index < len(lst):
            node = queue[front]
            front = front + 1

            item = lst[index]
            index = index + 1
            if item != None:
                leftNumber = item
                node.left = TreeNode(leftNumber)
                queue.append(node.left)

            if index >= len(lst):
                break

            item = lst[index]
            index = index + 1
            if item != None:
                rightNumber = item
                node.right = TreeNode(rightNumber)
                queue.append(node.right)
        return root

# Adjust the Solution4 class to use find_node within the lowestCommonAncestor method
class Solution(object):
    def find_node(self, root, value):
        if root is None:
            return None
        if root.val == value:
            return root
        found = self.find_node(root.left, value)
        if found is not None:
            return found
        return self.find_node(root.right, value)

    def lowestCommonAncestor(self, root, p, q):
        parent = {root: None}
        stack = [root]

        # Step 1: DFS to find p and q
        while stack:
            if p in parent and q in parent:
                break
            node = stack.pop()
            if node:
                if node.left:
                    parent[node.left] = node
                stack.append(node.left)
                if node.right:
                    parent[node.right] = node
                stack.append(node.right)

        # Step 2: Find ancestors for p using parent pointers
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]

        return q


# Initialize the Solution4 object
sol = Solution()
# Create tree
root = TreeNode().create_tree([3,5,1,6,2,0,8,None,None,7,4])
p_value = 7
q_value = 6
# Call the lowestCommonAncestor function with TreeNode instances
print(sol.lowestCommonAncestor(root, p_value, q_value))

