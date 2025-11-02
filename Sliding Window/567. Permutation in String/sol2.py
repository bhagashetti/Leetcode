class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i =0 
        j = 0
        n1 = len(s1)
        n2 = len(s2)
        d = {}
        for char in s1:
            d[char] = 1+ d.get(char,0)
        def checkPermutattion(l):
            d1 = {}
            for i in range(l,l+n1):
                d1[s2[i]] = 1+d1.get(s2[i],0)
            return d1 == d
        while j < n2-n1+1 :
            if s2[j] in d:
                flag = checkPermutattion(j)
                if flag :
                    return True
            j+=1
        return False
            

        