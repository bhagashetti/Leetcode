# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        if not head:
            return 
        dummyNode.next = head
        prev = dummyNode
        curr = head
        while curr and curr.next:
            next_node = curr.next
            prev.next = next_node
            curr.next = next_node.next
            next_node.next = curr
            prev = curr
            curr = curr.next
        return dummyNode.next

