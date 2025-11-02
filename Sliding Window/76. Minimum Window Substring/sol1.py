class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        count = 0
        d = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        d.update({chr(c): 0 for c in range(ord('A'), ord('Z') + 1)})
        for char in t:
            d[char] = 1+d.get(char,0)
        left = 0
        right = 0
        startingIndex = -1
        min_length = float('inf')
        print(d)
        while right < n1:
            if d[s[right]] > 0:
                count+=1
            d[s[right]]-=1
            while count == n2:
                if right-left+1 < min_length:
                    min_length = right-left+1
                    startingIndex = left
                d[s[left]]+=1
                if d[s[left]] > 0:
                    count-=1
                left+=1
            right+=1
        if startingIndex == -1:
            return ""
        else:
            return s[startingIndex:startingIndex+min_length]
                    


