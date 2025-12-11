class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        sum = 0
        res = 0
        n = len(nums)
        for i in range(n):
            sum+=nums[i]
            rem = sum % k
            if rem in count:
                res+=count[rem]
            count[rem] = 1+ count.get(rem,0)
        return res

        