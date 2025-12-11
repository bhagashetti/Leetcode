stack = []
nums = [2,1,3,4,5,57,8]

# elements will decreasing order top ele(last ele of list) will largest element 
# while pushing eleement in stack we should check wheather top element is greater  or not  


for num in nums:
    while stack and stack[-1] < num:
        stack.pop()
    stack.append(num)

