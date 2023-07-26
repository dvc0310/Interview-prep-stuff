class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'
    

def list_to_linked_list(lst):
    if not lst:  # if list is empty
        return None

    head = Node(lst[0])
    current_node = head
    for value in lst[1:]:
        new_node = Node(value)
        current_node.next = new_node
        current_node = new_node
    return head

def print_linked_list(node):
    while node:
        print(node.value, end=' ')
        node = node.next
    print()



head = [1,2,3,4,5]

head = list_to_linked_list(head)  

def oddEven(head):
    evenHead = head
    oddHead = head.next
    even_curr = evenHead
    odd_curr = oddHead

    while even_curr.next and even_curr.next.next:
        even_curr.next = even_curr.next.next
        if odd_curr.next != None:
            if odd_curr.next.next != None:
                odd_curr.next = odd_curr.next.next
            else:
                odd_curr.next = None
                even_curr = even_curr.next
                break
        even_curr = even_curr.next
        odd_curr = odd_curr.next
    
    even_curr.next = oddHead

    return evenHead

print(oddEven(head))