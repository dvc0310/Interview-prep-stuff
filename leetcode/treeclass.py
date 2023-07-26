from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
    
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

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def search(self, root, val):
        if root is None:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    def delete(self, val):
        self.root = self._delete(val, self.root)

    def _delete(self, val, node):
        if node is None:
            return node

        if val < node.val:
            node.left = self._delete(val, node.left)
        elif val > node.val:
            node.right = self._delete(val, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                current = node.right
                while current.left is not None:
                    current = current.left
                node.val = current.val
                node.right = self._delete(node.val, node.right)
        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorderTraversal(self, start, traversal=""):
        if start:
            traversal = self.inorderTraversal(start.left, traversal)
            traversal += (str(start.val) + "-")
            traversal = self.inorderTraversal(start.right, traversal)
        return traversal
    