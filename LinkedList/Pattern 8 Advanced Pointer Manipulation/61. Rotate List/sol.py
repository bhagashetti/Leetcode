# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n+=1
            temp = temp.next
        if n > 0:
            k = k % n
        if k == 0 or n == 0 :
            return head
        if not head:
            return head
        
        dummyNode = ListNode()
        dummyNode.next = head
        while k > 0:
            fast = dummyNode.next
            prev = None
            while fast.next:
                prev = fast
                fast = fast.next
            if prev:
                prev.next = None
            next = dummyNode.next
            dummyNode.next = fast 
            fast.next =  next
            k-=1
        return dummyNode.next
          
        