class Solution:
    def isPalindrome(self, x: int) -> bool:
        count = []
        if x<0:
            x= (-1) * x
            count.append(-1)

        while x >0:
            rem = x  %10
            count.append(rem)
            x = x//10
        left  = 0
        right = len(count) -1
        while left < right:
            if count[left] != count[right]:
                return False
            left+=1
            right-=1
        return True
        





        