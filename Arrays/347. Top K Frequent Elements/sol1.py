class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        count = dict(sorted(count.items(), key=lambda item: item[1],reverse=True))
        result = []

        for key in count:
            if k > 0:
                result.append(key)
                k-=1
        return result

    
        

        