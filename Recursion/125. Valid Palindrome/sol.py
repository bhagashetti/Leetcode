class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for char in s:
            if char.isalnum():
                res+=char.lower()
        n = len(res)
        def checkPalidrome(str,i):
            if i >= len(str)//2:
                return True
            
            if str[i] != str[n-i-1]:
                return False
            return checkPalidrome(str,i+1)
       
        return checkPalidrome(res,0)
     




        