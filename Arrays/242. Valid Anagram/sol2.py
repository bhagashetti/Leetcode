class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import defaultdict
        anagram = defaultdict(int)
        
        for a , b in zip(s,t):
            anagram[a]+=1
            anagram[b]-=1

        return any(anagram.values()) is False