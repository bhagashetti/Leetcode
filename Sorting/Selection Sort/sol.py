# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5


arr = [7, 5, 9, 2, 8]

n  = len(arr)

for i in range(n):
    minimum = arr[i]
    index = i

    for j in range(i,n):
        if arr[j] < minimum:
            minimum = arr[j]
            index = j 
    arr[i] , arr[index] = arr[index], arr[i]
print(arr)