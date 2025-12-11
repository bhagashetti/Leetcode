# Input Format: N = 6
# Result:   
# A 
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F

n = int(input("Enter a Number: "))
for i in range(n):
    num = 65+i
    for j in range(i+1):
        print(chr(num),end=" ")
    print()

