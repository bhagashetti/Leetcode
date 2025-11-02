# Input Format: N = 6
# Result:   
# 1
# 01
# 101
# 0101
# 10101
# 010101

n = int(input("Enter a Number: "))

for i in range(n):

    for j in range(i+1):
        if i % 2 !=0:
        
            if j % 2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        else:
            if j % 2 !=0:
                print(0,end=" ")
            else:
                print(1,end=" ")
    print()
