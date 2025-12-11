
# Input Format: N = 6
# Result:   
# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************
n = int(input("Enter a Number"))
for i in range(1,n+1):
    star = n - i+1
    space = 2*i-2
    for j in range(star):
        print("*" , end=" ")
    for k in range(space):
        print(" ",end=" ")
    for f in range(star):
        print("*" , end=" ")
    print()
for i in range(1,n+1):
    space = 2*(n-i)
    star = i
    for j in range(star):
        print("*" , end=" ")
    for k in range(space):
        print(" ",end=" ")
    for f in range(star):
        print("*" , end=" ")
    
    print()

 