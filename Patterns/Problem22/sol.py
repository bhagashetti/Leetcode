# Input Format: N = 6
# Result:   
# 6 6 6 6 6 6 6 6 6 6 6 
# 6 5 5 5 5 5 5 5 5 5 6 
# 6 5 4 4 4 4 4 4 4 5 6 
# 6 5 4 3 3 3 3 3 4 5 6 
# 6 5 4 3 2 2 2 3 4 5 6 
# 6 5 4 3 2 1 2 3 4 5 6 
# 6 5 4 3 2 2 2 3 4 5 6 
# 6 5 4 3 3 3 3 3 4 5 6 
# 6 5 4 4 4 4 4 4 4 5 6 
# 6 5 5 5 5 5 5 5 5 5 6 
# 6 6 6 6 6 6 6 6 6 6 6


n = int(input("Enter a Number"))
index = 2*n-1
for i in range(index):
    for j in range(index):
        top = i
        left = j
        bottom = 2*n - 2-i
        right = 2*n-2-j

        val = n-(min(min(top,bottom),min(left,right)))
        print(val,end=" ")
    print()
       
      
