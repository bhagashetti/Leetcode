class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        n = len(s)
        max_len = 0
        for i in range(n):
            if s[i] in seen and seen[s[i]] >= left:
                left = seen.get(s[i])+1
            max_len = max(max_len,(i-left+1))
            seen[s[i]] = i
        return max_len

