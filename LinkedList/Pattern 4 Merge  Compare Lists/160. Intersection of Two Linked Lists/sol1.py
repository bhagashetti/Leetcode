# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        
        lenA = 0
        temp1 = headA
        while temp1:
            lenA+=1
            temp1 = temp1.next
        lenB = 0
        temp2 = headB
        while temp2:
            lenB+=1
            temp2 = temp2.next
        temp1 = headA
        temp2 = headB
        if lenA > lenB:
            diff = lenA - lenB
            while diff:
                temp1 = temp1.next
                diff-=1
        elif lenB > lenA:
            diff = lenB - lenA
            while diff :
                temp2 = temp2.next
                diff-=1
        
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None
        
        
        