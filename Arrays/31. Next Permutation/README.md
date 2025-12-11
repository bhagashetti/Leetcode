Next Permutation

Permutations are possible combination of elements in array

example 
Array = [1,2,3]

permutations are below

1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1 

next permutation means - if we sort all combinations , for given example , its next order of elements (lelexicographical)

Example - given 3,1,2  - next permutation - 3,2,1


Solution Approach

step1:
------------------

find index  , iterate over the array from last 
find element arr[i] < arr[i+1]

mark index = i
break


step2:
--------------------

if you didnot find index

then reverse the Array , that is answer

else if you find the index , iterate the array from end till index(include)
find element which is greater than element at index 

swap those elements 
break


step3:
----------------------------------------------

iterate over the array from index+1 till end , reverse the array

