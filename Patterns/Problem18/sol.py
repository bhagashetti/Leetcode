# Input Format: N = 6
# Result:   
# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F

n = int(input("Enter a Number: "))

for i in range(n):
    num = 64+n - i
    for j in range(i+1):
        print(chr(num+j),end=" ")
    print()
