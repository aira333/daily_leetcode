# copy list with random pointer

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
        
def copyRandomList(head):
    if not head:
        return None
    
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
        
    current = head
    while current:
        current.next.random = current.random.next if current.random else None
        current = current.next.next
        
    current = head
    copy_head = head.next
    copy_current = copy_head
    while current:
        current.next = current.next.next
        current = current.next
        copy_current.next = copy_current.next.next if copy_current.next else None
        copy_current = copy_current.next
        
    return copy_head