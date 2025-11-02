

name = input("Enter a Name: ")

n = int(input('Enter a Number: '))

def printName(name,n,i):
    if i > n:
        return 
    print(name)
    printName(name,n,i+1)
printName(name,n,1)