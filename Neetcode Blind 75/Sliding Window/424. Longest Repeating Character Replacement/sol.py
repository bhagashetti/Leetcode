class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = [0] * 26
        left = 0
        length = 0
        for right in range(n):
            count[ord(s[right])-65]+=1
            while (right-left+1)-max(count) > k:
                count[ord(s[left])-65] -=1
                left+=1
            length = max(length , right-left+1)
        return length
            