# Input Format: N = 6
# Result:     
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

n=int(input("Enter a Number: "))

for i in range(n):
    star = 2*n-2*i-1
    for k in range(i):
        print(" ",end=" ")
    for j in range(star):
        print("*",end=" ")
   
    
    print()

