class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

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

