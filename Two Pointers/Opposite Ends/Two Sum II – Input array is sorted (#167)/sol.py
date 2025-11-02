class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            val = numbers[left] + numbers[right]
            if val > target:
                right-=1
            elif val < target:
                left+=1
            else:
                return [left+1,right+1]
        
