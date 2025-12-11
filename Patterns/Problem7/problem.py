# Input Format: N = 6
# Result:
#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********


n = int(input("Enter a Number: "))

for i in range(n):
    space = n-i
    for j in range(space):
        print(" ",end=" ")
    star = i+i+1
    for k in range(star):
        print("*" , end=" ")
    print()



