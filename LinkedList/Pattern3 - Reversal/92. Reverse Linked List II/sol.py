# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        count = 0
        start = None
        end = None
        prev_l = None
        while temp:
            count+=1
            if count == left:
                prev_l = temp
                start = temp.next
            if count == right:
                end = temp.next  
            
            temp = temp.next
        
        end_list = end.next
        end.next = None
        prev_l.next = None
        curr = start
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        prev_l.next = prev
        start.next = end_list
        return dummy.next











            


        


       