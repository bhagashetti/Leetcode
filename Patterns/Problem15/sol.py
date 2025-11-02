# Input Format: N = 6
# Result:   
# A B C D E F
# A B C D E 
# A B C D
# A B C
# A B
# A


n = int(input("Enter a Number: "))

for i in range(n,-1,-1):
    
    for j in range(i):
        num = 65+j
        print(chr(num),end=" ")

    print()
