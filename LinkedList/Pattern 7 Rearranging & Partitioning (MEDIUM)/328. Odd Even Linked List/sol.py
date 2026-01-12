# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 1

        res = []
        res.append(0)
        dummyNode = ListNode()
        while temp:
            next = temp.next
            node = temp
            node.next = None
            res.append(node)
            temp = next
        n = len(res)
        temp = dummyNode
        for i in range(1,n,2):
            temp.next = res[i]
            temp = temp.next
        for j in range(2,n,2):
            temp.next = res[j]
            temp = temp.next
        return dummyNode.next


        