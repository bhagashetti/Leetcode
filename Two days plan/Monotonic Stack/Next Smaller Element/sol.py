
def nextSmallerEle(arr):
    stack = []
    d = {}
    n = len(arr)
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            d[stack.pop()] = i
        stack.append(i)
    result = [d.get(i,-1) for i in range(n)]
    for i in range(n):
        if result[i] != -1:
            result[i] = arr[result[i]]
            
    return result
		