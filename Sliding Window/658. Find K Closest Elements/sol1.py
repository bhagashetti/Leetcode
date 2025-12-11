class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0   
        n = len(arr)
        right = k
        while right < n:
            val1 = abs(x-arr[left])
            val2 = abs(x-arr[right])
            if val2 < val1:
                left = right - k + 1
            elif val2 > val1:
                break    
                print(left,right)
            right+=1
        output =[]
        while left < n and k > 0:
            output.append(arr[left])
            k-=1
            left+=1  
        return output
            



        