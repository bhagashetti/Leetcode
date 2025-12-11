class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        minimum_length = float('inf')
        for s in strs:
            if len(s) < minimum_length:
                minimum_length = len(s)
        longest_string = ''
        
        for i in range(minimum_length):
            s = strs[0][i]
            for j in range(1,n):
                if s == strs[j][i]:
                    continue
                else:
                   return longest_string
            longest_string+=s
        return longest_string
                

                    

                



       
        