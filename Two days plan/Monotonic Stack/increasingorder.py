stack = []
nums = [1,5,6, 3,2,7, 8,9]

for num in nums:
    while stack and stack[-1] > num:
        stack.pop()
    stack.append(num)
print(stack)


# increasing order means top , elements should increas from bottom to top 

# top eleme (last ele of list )should smaller

# whenever we enter new element we should check wheather is greater than top element