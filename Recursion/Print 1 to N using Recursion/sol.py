

n = int(input('Enter a Number: '))

def printN(n,i):
    if i > n:
        return 
    print(i)
    printN(n,i+1)
printN(n,1)