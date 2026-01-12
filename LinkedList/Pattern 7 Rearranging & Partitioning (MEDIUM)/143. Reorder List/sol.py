# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        first = []
        while fast and fast.next:
            next = slow.next
            nextTonext = fast.next.next
            node = slow
            node.next = None
            first.append(node)
            slow = next
            fast = nextTonext
        second = []
        while slow:
            next = slow.next
            node = slow
            node.next = None
            second.append(node)
            slow = next
        n1 = len(first)
        n2 = len(second)
        i = 0
        dummyNode = ListNode()
        temp = dummyNode
        while i < n1:
            temp.next = first[i]
            temp = temp.next
            temp.next = second[n2-1-i]
            temp = temp.next
            i+=1
        j = n2 -1 -i
        while j > -1:
            temp.next = second[j]
            temp = temp.next
            j-=1
        return dummyNode.next

