n = int(input("Enter a Number: "))

temp = n

count = 0

while temp > 0:
    count+=1
    temp = temp // 10
    
sum = 0 

temp = n 

while temp > 0:
    rem = temp % 10
    temp = temp // 10
    sum += pow(rem,count)
if sum == n:
    print(True)
else:
    print(False)