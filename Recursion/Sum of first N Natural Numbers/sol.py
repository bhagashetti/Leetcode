# Example 2:
# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=21
n = int(input('Enter a Number: '))
sum = 0
def sumN(i,n,sum):
    if i > n:
        print(sum)
        return
    sum+=i
    sumN(i+1,n,sum)
sumN(1,n, sum)

