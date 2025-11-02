# Example 2:
# Input: N = 8 , Arr[] = {4,6,2,5,7,9,1,3}
# Output: 1 2 3 4 5 6 7 9
# Explanation: After sorting the array becomes 1, 3, 4, 7, 9

def quickSort(arr,low,high):
    if low < high:
        pIndex  = partition(arr,low,high)
        quickSort(arr,low,pIndex-1)
        quickSort(arr,pIndex+1,high)
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <=high-1:
            i+=1
        while arr[j] > pivot and j >= low:
            j-=1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
        
    arr[low],arr[j] = arr[j] ,arr[low]
    return j
arr = [4,6,2,5,7,9,1,3]
print(arr)
quickSort(arr,0,len(arr)-1)
print(arr)

    



