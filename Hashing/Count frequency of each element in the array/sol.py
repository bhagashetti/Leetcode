arr = [10,5,10,15,10,5]

d = {}
for num in arr:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
print(d)