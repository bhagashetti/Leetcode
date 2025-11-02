class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = [[] for i in range(len(nums)+1)]
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        for key in d:
            count[d[key]].append(key)
        print(count)
        for i in range(len(count)-1,-1,-1):
            if k > 0:
                if count[i] == []:
                    continue
                temp = count[i]
                for ele in temp:
                    result.append(ele)
                    k-=1
            else:
                break
        return result
        