class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res+=str(n)
            res+='#'
            res+=s
            
            
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        temp = ''
        n = len(s)
        i = 0
        while i < n:
            l = ''
            while i < n and s[i] != '#':
                if s[i].isnumeric():
                    l+=s[i]
                i+=1
            l = int(l)
            result.append(s[i+1:i+1+l])
            i = i+1+l
        return result

