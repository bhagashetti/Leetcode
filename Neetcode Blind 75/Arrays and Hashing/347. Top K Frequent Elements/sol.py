class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        n = len(nums)
        for num in nums:
            d[num] = 1+ d.get(num,0)
        count = [[] for _ in range(n + 1)]
        for key in d:
            count[d[key]].append(key)
        result = []
        for i in range(n,-1,-1):
            if count[i] != []:
                if k > 0:
                    for val in count[i]:
                        result.append(val)
                        k-=1
                else:
                    break
        return result


        