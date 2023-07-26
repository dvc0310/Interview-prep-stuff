import heapq
class MedianMaintainer:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.median = None
    
    def add(self, node):
        if not self.minheap and not self.maxheap:
            if self.median == None:
                self.median = node
            else:
                heapq.heappush(self.minheap, node)
            return
        
        if node > self.median:
            heapq.heappush(self.minheap, node)
        else:
            heapq.heappush(self.maxheap, -node)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -self.median)
            self.median = heapq.heappop(self.minheap)

        if len(self.minheap) + 1 <= len(self.maxheap):
            heapq.heappush(self.minheap, self.median)
            self.median = -heapq.heappop(self.maxheap)
    
    def find_median(self):
        return self.median
    
    def remove_median(self):
        res = self.median
        if not self.maxheap and not self.minheap:
            self.median = None
            return res
        if len(self.minheap) > len(self.maxheap):
            self.median = heapq.heappop(self.minheap)
        else:
            self.median = -heapq.heappop(self.maxheap)
        
        return res
    

med = MedianMaintainer()
arr = [5, 9, 6, 20, 30, 2]
for num in arr:
    med.add(num)

med.find_median()

for _ in arr:
    print(med.remove_median())

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
    
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parents = {}
        parents[root.val] = None
        self.dfs(root, p, q, parents)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q
    
    def dfs(self, root, p, q, parents):
        stack = [root]
        pfound = False
        qfound = False

        while stack:
            node = stack.pop()
            if node.val == p:
                pfound = True
            if node.val == q:
                qfound = True
            if pfound and qfound:
                return
            if node.right:
                stack.append(node.right)
                parents[node.right.val] = node.val
            if node.left:
                stack.append(node.left)
                parents[node.left.val] = node.val
            
    def find_node(self, root, value):
        if root is None:
            return None
        if root.val == value:
            return root
        found = self.find_node(root.left, value)
        if found is not None:
            return found
        return self.find_node(root.right, value)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        ancestor = None
        pvisit = False
        qvisit = False
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if stack and pvisit and qvisit and visited:
                ancestor = node
                while stack and stack[-1][1]:
                    ancestor, _ = stack.pop()
                return ancestor
            else:
                if not visited:
                    # First, check if either of the children are p or q.
                    if node.right:
                        if node.right.val == p:
                            pvisit = True
                        elif node.right.val == q:
                            qvisit = True
                    if node.left:
                        if node.left.val == p:
                            pvisit = True
                        elif node.left.val == q:
                            qvisit = True
                    
                    
                    stack.append((node, True))

                    # If the children are not p or q, they should still be added to the stack.
                    if node.right and node.right.val != p and node.right.val != q:
                        stack.append((node.right, False))
                    if node.left and node.left.val != p and node.left.val != q:
                        stack.append((node.left, False))

        if pvisit and not qvisit:
            return p
        elif qvisit and not pvisit:
            return q
        return ancestor

# Initialize the Solution4 object
sol = Solution()
# Create tree
root = TreeNode().create_tree([3,5,1,6,2,0,8,None,None,7,4])
p_value = 5
q_value = 0
# Call the lowestCommonAncestor function with TreeNode instances
print(sol.lowestCommonAncestor(root, p_value, q_value))
    


    