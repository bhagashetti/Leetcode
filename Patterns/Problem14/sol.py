# Input Format: N = 6
# Result:   
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F

n  = int(input("Enter a Number"))

for i in range(n):
    num = 65
    for j in range(i+1):
        print(chr(num),end=" ")
        num= num+1
    print()

