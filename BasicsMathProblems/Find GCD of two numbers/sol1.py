n1 = int(input("Enter a Number: "))
n2 = int(input("Enter a Number: "))


while n1 > 0 and n2 > 0:
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1
if n1 == 0:
    print(n2)
else:
    print(n1)