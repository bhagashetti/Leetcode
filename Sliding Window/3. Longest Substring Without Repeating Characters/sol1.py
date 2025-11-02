class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left  = 0
        seen = set()
        n = len(s)
        max_len = 0
        print(n)
        for i in range(n):
            if s[i] in seen:
                l = i-left
                if l > max_len:
                    max_len = l
                while left < n and s[i] in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(s[i])
            l = i-left+1
            if l > max_len:
                max_len = l
        return max_len 
            

        