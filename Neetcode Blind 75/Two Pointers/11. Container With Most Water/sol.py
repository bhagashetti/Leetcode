class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maximum_water = 0
        left =0
        right = n-1
        while left < right:
            water = min(height[left],height[right]) *(right-left)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            maximum_water = max(maximum_water,water)
        return maximum_water