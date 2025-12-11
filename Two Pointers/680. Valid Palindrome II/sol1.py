class Solution:
    def validPalindrome(self, s: str) -> bool:
        count  = 0
        n = len(s)
        left = 0
        right = n-1
        def checkPalidrome(s):
            left = 0 
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        while left < right:
            if s[left] != s[right] and count > 0:
                return False
            elif s[left] != s[right]:
                print(s[left+1:right+1])
                ans1 = checkPalidrome(s[left+1:right+1])
                ans2 = checkPalidrome(s[left:right])
                return ans1 or ans2 
            else:
                left+=1
                right-=1 
        return True
    
        