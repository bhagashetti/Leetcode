# Input Format: N = 6
# Result:   
# ******
# *    *
# *    *
# *    *
# *    *
# ******

n = int(input("Enter a Number: "))

for i in range(1,n+1):
    if i == 1 or i == n:
        star = n
        space = 0
        for j in range(star):
            print("*",end=" ")

    else:
        star = 1
        space = n - 2
        for j in range(star):
            print("*",end=" ")
        for k in range(space):
            print(" ",end=" ")
        for j in range(star):
            print("*",end=" ")
    print()
        



    

