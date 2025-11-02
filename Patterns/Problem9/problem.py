# Input Format: N = 6
# Result:   
#      *
#     ***
#    ***** 
#   *******
#  *********
# ***********  
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

n = int(input("Enter Number: "))

for i in range(n):
    space = n-i-1
    for j in range(space):
        print(" " , end=" ")
    star = i+i+1
    for k in range(star):
        print("*",end=" ")
    print()
for i in range(n):
    star = n*2 -i*2 -1
    for j in range(i):
        print(" ",end=" ")
    for k in range(star):
        print("*",end=" ")
    print()