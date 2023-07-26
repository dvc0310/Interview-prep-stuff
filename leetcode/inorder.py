class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Node({self.data})"


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self._print(self.root)

    def _print(self, node):
        if node is None:
            return ''
        else:
            left_subtree = self._print(node.left)
            right_subtree = self._print(node.right)
            return f"{left_subtree} {node.data} {right_subtree}".strip()

    def __repr__(self):
        return f"BST({self.__str__()})"

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)
                
    def morris_inorder_traversal(self):
        current = self.root
        
        while current is not None:
            if current.left is None:
                print(current.data)
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right

                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    print(current.data)
                    current = current.right

bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

bst.morris_inorder_traversal()  # This will print the BST as a min-heap

        