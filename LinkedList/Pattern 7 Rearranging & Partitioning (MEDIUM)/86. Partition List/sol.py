# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []
        more = []
        temp = head
        while temp:
            next = temp.next
            if temp.val < x:
                node = temp
                node.next = None
                less.append(node)
            else:
                node = temp
                node.next = None
                more.append(node)
            temp = next
        dummyNode = ListNode()
        temp = dummyNode
        for i in range(len(less)):
            temp.next = less[i]
            temp = temp.next
        for j in range(len(more)):
            temp.next = more[j]
            temp = temp.next
        return dummyNode.next



        
        


        