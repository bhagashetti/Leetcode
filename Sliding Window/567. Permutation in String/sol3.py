class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        d1 = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        d2 = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        if n1 > n2:
            return False
        for i in range(n1):
            d1[s1[i]] = 1+ d1.get(s1[i],0)
        for j in range(n1):
            d2[s2[j]] = 1+ d2.get(s2[j],0)
        j = n1
        if d1==d2:
            return True
        i= 0
        while j < n2:
            d2[s2[i]] -=1
            d2[s2[j]] = 1+ d2.get(s2[j],0)
            if d1 == d2:
                return True
            j+=1
            i+=1
        return False