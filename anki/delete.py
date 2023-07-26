class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


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

    def inorderTraversal(self, start, traversal=""):
        if start:
            traversal = self.inorderTraversal(start.left, traversal)
            traversal += (str(start.val) + " ")
            traversal = self.inorderTraversal(start.right, traversal)
        return traversal
    
    def delete(self, val):
        self._delete(val, self.root)

    def _delete(self, val, node):
        if node is None:
            return None
        
        if val > node.val:
            node.left = self._delete(val, node.left)
        elif val < node.val:
            node.right = self._delete(val, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            curr = node.right
            while curr.left != None:
                curr = curr.left
            node.val = curr.val
            node.right = self._delete(val, node.right)

        return node
    
bt = BinaryTree(40)
bt.insert(20)
bt.insert(60)
bt.insert(10)
bt.insert(30)
bt.insert(50)
bt.insert(70)
bt.insert(35)
bt.insert(45)
bt.delete(20)
print(bt.inorderTraversal(bt.root))