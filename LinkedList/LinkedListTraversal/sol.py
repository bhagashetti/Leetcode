class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_traversal(head):
    current = head
    while current:
        print(current.val)
        current = current.next


head = ListNode(1, ListNode(2, ListNode(3)))

linked_list_traversal(head)
