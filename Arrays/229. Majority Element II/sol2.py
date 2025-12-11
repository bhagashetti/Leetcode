class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = 0
        count2 = 0
        majority_ele1 = None
        majority_ele2 = None
        n = len(nums)
        for i in range(n):
            if count1 == 0 and nums[i] != majority_ele2:
                count1 = 1
                majority_ele1 = nums[i]
            elif count2 == 0 and nums[i] != majority_ele1:
                count2 = 1
                majority_ele2 = nums[i]
            elif nums[i] == majority_ele1:
                count1+=1
            elif nums[i] == majority_ele2:
                count2+=1
            else:
                count1-=1
                count2-=1
        count1 = 0
        count2 = 0
        max_count = n//3
        res = []
        for num in nums:
            if num == majority_ele1:
                count1+=1
            elif num == majority_ele2:
                count2+=1
        if count1 >  max_count :
            res.append(majority_ele1)
        if count2 > max_count:
            res.append(majority_ele2)
        return res

            


