n = int(input("Enter a Number: "))
factorial = 1
def fact(i,n,factorial):
    if i > n:
        print(factorial)
        return
    factorial *= i
    fact(i+1,n,factorial)
fact(1,n,factorial)
