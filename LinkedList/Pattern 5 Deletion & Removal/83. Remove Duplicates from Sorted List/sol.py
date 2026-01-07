
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        temp = head
        prev = dummyNode

        while temp and temp.next:
            if  temp.val == temp.next.val:
                if temp.next:
                    prev.next = temp.next
                else:
                    prev.next = None
            else:
                prev = temp
            temp = temp.next
        return dummyNode.next
                

            


        