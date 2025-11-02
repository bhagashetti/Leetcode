class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        index = None
        n = len(nums)
        output = []
        if k > n:
            return 
        max_ele = float('-inf')
        for i in range(k):
            if max_ele <= nums[i]:
                max_ele = nums[i]
                index = i
        output.append(max_ele)
        while right < n:
            if nums[left] != max_ele:
                if max_ele < nums[right]:
                    max_ele = nums[right]
                    index = right
            elif nums[left] == max_ele and index != left:
                if max_ele < nums[right]:
                    max_ele = nums[right]
                    index = right    
            elif  nums[left] == max_ele and left == index:
                i= index+1
                j = right
                max_ele = float('-inf')
                while i <= j:
                    if nums[i] > nums[j]:
                        if max_ele <  nums[i]:
                            max_ele = nums[i]
                            index  = i
                        j-=1
                    else:
                        if max_ele <  nums[j]:
                            max_ele = nums[j]
                            index = j
                        i+=1
            right+=1
            left+=1
            output.append(max_ele)
        return output


                
                
                    


            


