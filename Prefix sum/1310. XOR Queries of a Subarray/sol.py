class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        for i in range(1,n):
            arr[i] = arr[i] ^ arr[i-1]
        l = len(queries)
        output = []
        for i in range(l):
            i1 = queries[i][0]
            i2 = queries[i][1]
            if i1 > 0:
                output.append(arr[i2] ^ arr[i1-1])
            elif i1 == 0:
                output.append(arr[i2])
        return output

        

        