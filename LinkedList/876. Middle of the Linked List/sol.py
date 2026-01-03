# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count = 0
        curr = head
        while curr:
            count+=1
            curr = curr.next
        mid = count / 2
        if type(mid) == 'int':
            mid = mid+1
        else:
            mid = mid+1
            mid = int(mid)
        count = 0
        curr = head
        while curr:
            count+=1
            if count == mid:
                return curr
            curr = curr.next
        
        


        