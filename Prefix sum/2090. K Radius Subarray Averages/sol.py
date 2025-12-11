class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        prefix_sum = [0] * (n+1)
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        right = k*2
        left = -1
        i = k
        res = [-1] *n
        d = k*2+1
        while right < n:
            sum = prefix_sum[right]
            if left > -1:
                sum -=prefix_sum[left]
            res[i] = sum//d
            i+=1
            left+=1
            right+=1
        return res




    