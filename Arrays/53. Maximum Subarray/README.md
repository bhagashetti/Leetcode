# Algorithm for this problem is Kadane's Algorithm

Approach:

1) Intialize maximum_sum with infinite negative value
2) iterate via nums
3) sum+=nums[i]
4) compare sum with maximum_sum
5) is sum < 0: sum=0

Intution is : if sum goes negative , sum wont get increse , we should make sum = 0