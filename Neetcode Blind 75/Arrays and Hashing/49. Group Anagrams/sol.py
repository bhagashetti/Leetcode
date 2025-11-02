class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp in d:
                d[temp].append(s)
            else:
                d[temp] = []
                d[temp].append(s)
        result = []
        for key in d:
            result.append(d[key])
        return result

        

        