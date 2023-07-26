import random
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def shuffle_linked_list(head):
    if not head or not head.next:
        return head

    # Step 1: split the list into two halves
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = None

    # Step 2: shuffle each half independently
    first = shuffle_linked_list(head)
    second = shuffle_linked_list(slow)

    # Step 3: merge the two halves, selecting nodes alternately
    dummy = Node(0)
    current = dummy
    while first and second:
        if random.randint(0, 1):
            current.next = first
            first = first.next
        else:
            current.next = second
            second = second.next
        current = current.next

    current.next = first if first else second
    return dummy.next
