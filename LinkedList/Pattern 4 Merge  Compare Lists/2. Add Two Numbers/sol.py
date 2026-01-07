# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        num1 = 0
        pow = 1
        while temp1:
            num1+=pow * temp1.val
            pow = pow * 10
            temp1 = temp1.next
        temp2 = l2
        num2 = 0
        pow = 1
        while temp2:
            num2+=pow * temp2.val
            pow = pow * 10
            temp2 = temp2.next
        sum = num1 + num2
        if sum == 0:
            dummyNode = ListNode()
            node = ListNode(0)
            dummyNode.next = node
            return dummyNode.next

        res = []
        while sum:
            rem = sum % 10
            res.append(rem)
            sum = sum//10
        dummyNode = ListNode()
        head = dummyNode
        for num in res:
            node = ListNode(num)
            head.next = node
            head = head.next
        return dummyNode.next

