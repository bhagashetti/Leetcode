# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        temp1  = list1
        temp2 = list2
        head  = dummyNode
        while temp1 and temp2:
            if temp1.val < temp2.val:
                head.next = temp1
                temp1 = temp1.next
            else:
                head.next = temp2
                temp2 = temp2.next
            head = head.next
        while temp1:
            head.next = temp1

            head = head.next
            temp1 = temp1.next
        while temp2:
            head.next = temp2

            head = head.next
            temp2 = temp2.next
        return dummyNode.next

            
        