# Example 2:
# Input: N=6 arr[] = {10,20,30,40}


# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

n = int(input("enter a number: "))
arr = []
for i in range(n):
    arr.append(int(input("enter array element: ")))

res = []
def reverseArray(arr,n,res):

    if n == -1 :
        print(res)
        return
    res.append(arr[n])
    reverseArray(arr,n-1,res)
    
reverseArray(arr,n-1,res)



