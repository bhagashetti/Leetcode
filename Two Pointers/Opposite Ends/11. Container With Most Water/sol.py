class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        most_water = 0

        while left < right:
            water = (right-left)*min(height[left],height[right])
            most_water = max(most_water,water)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return most_water

    


        