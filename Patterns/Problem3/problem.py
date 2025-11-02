# Input Format: N = 6
# Result:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


n = int(input("Enter a Number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()