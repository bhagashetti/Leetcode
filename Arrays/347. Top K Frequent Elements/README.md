sol1:  Using dictionary and sort the dictionary respective of items 
 time complexity : O(nlongn)


 sol2 : use max heap , push element in max_heap and pop element from max_heap until k == 0

 sol3: Bucket sort - take dictinary , count elemets d{ele: freq}
  
  take one more array size of (nums +1)

  index represents the frequency of elements , 

  append elements in array according to their frequency ( at index)

  traverse from last , print the elements untill k ==  0