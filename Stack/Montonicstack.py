nums = [2,4,2,1,6,7]
n = len(nums)
result = [-1] * n
stack = []
for i in range(n):
    while stack and stack[-1] > nums[i]:
        stack.pop()
    result[i] = stack[-1] if stack else -1
    stack.append(nums[i])
print(result)
