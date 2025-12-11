n = int(input("Enter a Number: "))

def PrintN(i):
    if i == 0:
        return 
    print(i)
    PrintN(i-1)
PrintN(n)
        