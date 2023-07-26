import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return ' -> '.join(nodes)

    def get_node(self, index):
        current = self.head
        for _ in range(index):
            if current:
                current = current.next
        return current

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverseList(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def shuffle(self):
        length = self.get_length()
        for i in range(length-1, -1, -1):
            j = random.randint(0, i)  # Not i + 1
            
            # Swap nodes at i and j
            i_node = self.get_node(i)
            j_node = self.get_node(j)
            
            i_node.value, j_node.value = j_node.value, i_node.value

    def isPalindromeImproved(self, head):
        if head is None or head.next is None:
            return True

        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        first_half, second_half = head, prev
        result = True
        while second_half is not None:
            if first_half.val != second_half.val:
                result = False
                break
            first_half = first_half.next
            second_half = second_half.next

        curr, prev = prev, None
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr 
            
        return result
    
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        
        double = head
        single = head
        prev = None
        
        while double is not None and double.next is not None:
            double = double.next.next
            prev = single
            single = single.next

        prev.next = single.next
        return head
    
    def pairSum(self, head):
        lst = []
        curr = head
        while curr:
            lst.append(curr.value)
            curr = curr.next
        l = 0
        r = len(lst) - 1
        maxSum = -999999999999
        while l < r:
            maxSum = max(maxSum, lst[l] + lst[r])
            l += 1
            r -= 1

        return maxSum

    
    
ll = LinkedList()
ll.add(4)
ll.add(2)
ll.add(2)
ll.add(3)
print(ll.pairSum(ll.head))

