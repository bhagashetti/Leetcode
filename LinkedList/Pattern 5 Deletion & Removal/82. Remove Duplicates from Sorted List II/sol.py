# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        prev = dummyNode
        dummyNode.next = head
        temp = head
        s = set()
        while temp and temp.next:
            if temp.val == temp.next.val:
                s.add(temp.val)
                while temp and temp.next and temp.val == temp.next.val:
                    prev.next = temp.next
                    temp = temp.next
            else:
                prev = temp
                temp = temp.next
        temp = head
        prev = dummyNode
        while temp:
            if temp.val in s:
                if temp.next:
                    prev.next = temp.next
                else:
                    prev.next = None
            else:
                prev = temp
            temp = temp.next
        return dummyNode.next
