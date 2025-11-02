class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
    
        reverse_number = 0
        temp = x
        if x < 0:
            temp = temp *(-1)

        while temp > 0:
            rem = temp % 10
            if reverse_number > (INT_MAX - rem) // 10:
                return 0
            reverse_number = reverse_number*10 + rem
            temp = temp //10
        if x < 0:
            reverse_number = -1 * reverse_number
        return reverse_number
 
            
        