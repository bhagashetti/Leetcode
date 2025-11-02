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
        i = 0
        n = len(s)
        res = []
        temp = ''
        while i < n:
            if s[i].isdigit():
                temp+=s[i]
                i+=1
            elif s[i] == '#':
                j = i+1
                res.append(s[j:j+int(temp)])
                i+=int(temp)+1
                temp = ''
        return res



        