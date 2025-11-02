class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum ={0:1}
        count = 0
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            ele = curr_sum - k
            count+=prefix_sum.get(ele,0)
            prefix_sum[curr_sum]  = 1+ prefix_sum.get(curr_sum,0)
        return count


        

       