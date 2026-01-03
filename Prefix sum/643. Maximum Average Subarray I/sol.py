class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] *n 
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
        res = []
        left = -1
        for j in range(k-1, n):
            if left == -1:
                res.append(prefix_sum[j]/k)    
            else:
                res.append((prefix_sum[j]-prefix_sum[left])/k)  
            left+=1
        return max(res)


        