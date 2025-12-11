arr = [5,4,3,2,1]

def bubblesort(arr,n):
    if n == 1:
        return 
    didSwap = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
            didSwap = 1
    if didSwap == 0:
        return
    bubblesort(arr,n-1)

    
bubblesort(arr,len(arr))
print(arr)