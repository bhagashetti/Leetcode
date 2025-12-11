arr = [5,4,3,2,1]

n = len(arr)

def Inseration(arr,i,n):
    if i==n:
        return 
    j = i
    
    while j > 0 and arr[j] < arr[j-1]:
        arr[j] , arr[j-1] = arr[j-1] , arr[j]
        j-=1
    Inseration(arr,i+1,n)
Inseration(arr,0,n)
print(arr)