class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] *n
        prefix[0] = arr[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + arr[i]
        sum = 0
        for i in range(n):
            sum+=arr[i]
        for i in range(2,n,2):
            left = -1
            for right in range(i,n):
                if left > -1:
                    sum+= prefix[right] - prefix[left]
                else:
                    sum+=prefix[right]
                left+=1
        
        return sum