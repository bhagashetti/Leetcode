
num = int(input("Enter a number: "))
def printN(n):
    if n == num:
        return
    print(n)
    printN(n+1)
printN(0)