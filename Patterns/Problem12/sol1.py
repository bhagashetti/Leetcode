# Input Format: N = 6
# Result:   
# 1          1
# 12        21
# 123      321
# 1234    4321
# 12345  54321
# 123456654321

n = int(input("Enter a Number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    space = 2*n-2*i
    for k in range(space):
        print(" ",end=" ")
    
    for m in range(i,0,-1):
        print(m,end=" ")
    
    print()
