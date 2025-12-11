# Input Format: N = 6
# Result:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1


n = int(input("Enter a Number: "))

for i in range(n,-1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()