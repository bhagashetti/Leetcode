# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp :
            count +=1
            temp = temp.next
        d = count - n 
        temp = head
        while d > 1:
            d-=1
            temp = temp.next
        if d == 0:
            return head.next
        if temp.next and temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        
        return head

        