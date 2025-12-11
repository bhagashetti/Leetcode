# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1,2,3,4,5


arr = [5,4,3,2,1]

n = len(arr)

for i in range(1,n):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j] , arr[j-1] = arr[j-1],arr[j]
print(arr)        

# below approach we should use because in best case inside loop wont even excute so time complexity for 
#  best case will O(N)
for i in range(n):
    j = i

    while j > 0 and arr[j] < arr[j-1]:
        arr[j] , arr[j-1] = arr[j-1],arr[j]
        j-=1
print(arr)

