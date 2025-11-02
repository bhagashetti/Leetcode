# Input: N = 5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting we get 1,2,3,4,5


arr = [5,4,3,2,1]
n = len(arr)

for i in range(n-1,0,-1):
    for j in range(0,i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

print("--------------------------------------")

for i in range(n):
    for j in range(n-1-i):
        print(j)
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
print(arr)

# Reducing Timecomplexity in best case (if array is sorted)
didSwap = 0
for i in range(n-1,0,-1):
    didSwap = 0
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
            didSwap = 1
    if didSwap == 0:
        break