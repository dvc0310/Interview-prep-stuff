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
            j = random.randint(0, i) 
            i_node = self.get_node(i)
            j_node = self.get_node(j)
            
            i_node.value, j_node.value = j_node.value, i_node.value

def addTwo(l1,l2):
    l1curr = l1.head
    l2curr = l2.head
    res = LinkedList()
    carry = 0
    while l1curr and l2curr:
        if l1curr.value + l2curr.value + carry < 10:
            res.add(carry + l1curr.value + l2curr.value)
            carry = 0
        else:
            res.add((l1curr.value + l2curr.value + carry) % 10)
            carry = 1
        l1curr = l1curr.next
        l2curr = l2curr.next

    while l1curr is not None:
        res.add(l1curr.value)
        l1curr = l1curr.next

    while l2curr is not None:
        res.add(l2curr.value)
        l2curr = l2curr.next
    
    return res


    