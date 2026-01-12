# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        left = 0
        right = len(res)-1
        while left < right:
            if res[left] != res[right]:
                return False
            left+=1
            right-=1
        return True



            

        