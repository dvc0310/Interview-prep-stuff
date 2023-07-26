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
