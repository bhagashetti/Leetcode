# Input Format: N = 6
# Result:   
#      A     
#     ABA    
#    ABCBA   
#   ABCDCBA  
#  ABCDEDCBA 
# ABCDEFEDCBA

n = int(input("Enter a Number: "))

for i in range(n):
    space = n - i-1
    for j in range(space):
        print(" ",end=" ")
    for k in range(i+1):
        print(chr(65+k),end=" ")
    for m in range(i-1,-1,-1):
        print(chr(65+m),end=" ")
    print()