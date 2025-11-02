What is Prefix Sum
-------------------------

Prefix sum is just running total 

Example 0 , 1, 2, 3, 4 
nums = [1 , 2, 3, 4, 5]

prefix sums like below
prefx_sum[0] = 0
[1] = 1
[2] = 1+2 = 3
[3] = 1+ 2 + 3 = 6
[4] = 1+2+3+4 = 10
[5] = 1+2+3+4+5 = 15

Prefix sum where each spot stores the sum upto that point


How to indentify Prefix sum Porblmes ( Kind of Problems can be solved using Prefix sum)
---------------------------------------------------------------------------------------
l = 5
r = 10

11 th index has includes 10th index 

6th index include 5 th index 
 we dont want value of 5th index 


1) Fast range sum 

Let's consider we have array , we want sum between l and r (l and r indexs of array) ( l inclusive and r exclusive)


first we create prefix sum like above 

then we will find sum = prefix_sum[r] - sum[l]

if both l and r inclusive

prefix_sum[r+1] - prefix_sum[l]

if l is exlusive and r is inclusive

prefix_sum[r+1] - prefix_sum[l+1]

both in exclusive

prefix_sum[r] - prefix_sum[l+1]
 
2) Number of Subarrays whose sum equal to K ( Array contains both negatives and positives values)


If array contains only positives values we can use sliding window techniques

if array contains negatives also ( we cant use sliding windows , beacuse in sliding window we wiil jsut move the pointer by adding , if it is negative it will become substrations)

steps
* take dict count[0] = 1  - beacuse - no elemnets (if k = 0 ) , we can consider this 
* iterate via Array , sum+=nums[i] ,  we want values k - sum = sum of all elements till i , we have to check sum- k = p there in count dictionary , if it is there , we have to take count of that to ans
* add this sum value in dictionary 

puesdo code 

count[0] = 1
sum = 0
nums=[]
ans = 0

for i in range(n):
    sum+=nums[i]
    p = sum-k
    if p in count:
        ans+= count[p]
    count[sum]  = 1+ count.get(sum,0)
return ans


3) Largest Subarray with sum k

Problem statement states that , given array , we have find longest subarray ( contigoues elements ) whose sum is equal to k 

we will maintain the dictionary with sum : index


psuedo code like below

nums = []
count = {0:-1}
sum = 0
ans = 0

for i in range(n):
    sum+=nums[i]
    p = sum - k
    if p in count:
        if ans <  i-count[p]:
            ans = i-count[p]
    if sum not in count:
        count[sum] = i


smallest array 



count = {0:-1}
sum = 0
best = 0
for i in range(n):
    sum+=nums[i]
    p = sum - k 
    if p in count:
        best = min(best , i-count[p])
    count[sum] = i
retrun best 
        

4) Subarrays sum divisible by K (sum % k == x)

Problem statement will be like : Count the number of subarrays whose sum is divisible k equal to x or 0


count[0] = 1
sum = 0

nums = []
res = 0

for ele in nums:
    sum+=ele
    rem = sum % k
    if rem in count:
        res+=count[rem]
    count[rem] = 1+ count.get(rem,0)
return count 

* if sum % k == x

sum = 0
res = 0

for ele in nums:
    sum += ele
    rem = sum % k
    
    # adjust remainder to always be positive
    rem = (rem + k) % k
    
    target = (rem - x + k) % k
    
    if target in count:
        res += count[target]
    
    count[rem] += 1



5) Equal number of A and B” (balance via recoding)

Problem statement : Find number of subarrays where it contains equal number of A and B elements 

Example:

nums = []
find subarrays where it contains equal 0's and equal 1's

nums =[1,2,0,4,5,0,1,3,5,0,1,2,1,5,6,0]

count = defaultdict()

sum  = res = 0

for ele in num :
    if ele == 0:
        sum-=1
    elif ele == 1:
        sum+=1
    res+=count[sum]
    count[sum]+=1
return res


6) Prefix XOR (same idea, for XOR)


count the number of subarrays whose(all elements of subarray) xor equal k

xor_val = 0

res = 0

nums = []
count = {0:1}

for ele in nums:
    xor_val^=ele
    p = xor_val ^ k
    if p in count:
        res+=count[p]
    count[xor_val] = 1+ count.get(xor_val)


7) Fixed-length window sums / averages with prefix

Problem statement : Given k ( window length) , Give sum / or avarage of nums with  window length k 

in that return maximum element 

nums = [1,2,3,4,4,5,5,6,6]
k = 3

prefix_sum = [0] *(n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i]+nums[i]

return max[prefix_sum[i+k]-prefix_sum[i] for i in range(n-k+1)]


8) 2D Prefix Sums (Matric Rectangles)


Problem statement : Sum of element from (r1,c1) to (r2,c2) in Given matrix

1 2 3
4 5 6
7 8 9


matrix = [[]]
cols , rows
prefix_sum = [[0]*(col+1) for _ in range(rows+1)]


for i in range(rows):
    for j in range(cols):
        prefix_sum[i+1][j+1] = matrix[i][j] + prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j]

sum from (r1,c1) to (r2,c2)

p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1]


9) Count submatrices whose sum = target (2D → 1D reduction)


Problem statement 

You are given an m x n integer matrix grid and an integer target.
Return the number of non-empty submatrices (axis-aligned, contiguous rows and columns) whose sum equals target.

Input: grid (may contain negatives, zeros, positives), target (int)

Output: integer count


from collections import defaultdict

def count_submatrices_sum_target(A, target):
    R, C = len(A), len(A[0])
    ans = 0

    # If taller than wide, iterate over rows; else flip to save time
    # Here we keep rows as the paired dimension
    for top in range(R):
        col = [0] * C
        for bot in range(top, R):
            # accumulate column sums between top..bot
            for c in range(C):
                col[c] += A[bot][c]

            # count subarrays in col with sum == target
            freq = defaultdict(int)
            freq[0] = 1
            S = 0
            for v in col:
                S += v
                ans += freq[S - target]
                freq[S] += 1

    return ans



10) Path sum in a tree (root-to-node)

number of paths whose sum = K” (paths must go downwards). - Tree node 

number of paths in Tree whose sum == k

def pathSum(root, K):
    seen = {0:1}
    def dfs(node, S):
        if not node: return 0
        S += node.val
        res = seen.get(S - K, 0)
        seen[S] = seen.get(S, 0) + 1
        res += dfs(node.left, S) + dfs(node.right, S)
        seen[S] -= 1
        return res
    return dfs(root, 0)
 

11)  Pivot / equilibrium index (left sum == right sum)


total = sum(nums)

left = 0

for i in range(n):
    if left == total - left - nums[i]:
        return i
    left+=nums[i]


12) Max subarray sum via prefix-min (Kadane variant)


Given an integer array (can include negatives), find the maximum possible sum of any contiguous subarray.


[−2,1,−3,4,−1,2,1,−5,4] → best is [4, −1, 2, 1] with sum 6.


Intuntion is 

sum[l,r] = prefix[r+1] - prefix_sum[l]

if we want maximu mean we should take min ( prefix_l so far)

pref = 0
best = 0
min_prefix_sum = 0
best = float('inf')

for i in range(n):
    pref +=nums[i]
    best = max(best , pref- min_pre_sum)
    min_pre_sum = min(min_pre_sum, pref)
return best 


13) Shortest subarray with sum ≥ K (with negatives) — monotonic deque


“minimum length subarray with sum ≥ K” and numbers may be negative.


Given an integer array nums (can include negatives) and an integer K, find the shortest length of any contiguous subarray whose sum is ≥ K. If none exists, return -1.


from collections import deque

def shortest_subarray_at_least_k(nums, K):
    n = len(nums)
    # prefix sums P[0] = 0, P[i+1] = sum(nums[:i+1])
    P = [0] * (n + 1)
    for i in range(n):
        P[i+1] = P[i] + nums[i]

    dq = deque()  # stores indices into P, with increasing P values
    ans = float('inf')

    for i in range(n + 1):
        # 1) satisfy condition: shrink from front if we can hit ≥ K
        while dq and P[i] - P[dq[0]] >= K:
            ans = min(ans, i - dq.popleft())

        # 2) maintain increasing P: remove dominated tails
        while dq and P[i] <= P[dq[-1]]:
            dq.pop()

        # 3) add current index
        dq.append(i)

    return -1 if ans == float('inf') else ans


14) Difference array / range updates (Imos method) — prefix in reverse

Its reverse of prefix sum 

def apply_range_updates(n, updates):
    """
    n: length of array
    updates: list of (L, R, v) with 0 <= L <= R < n
    returns the final array after all range adds
    """
    diff = [0] * (n + 1)  # one extra slot to allow R+1
    for L, R, v in updates:
        diff[L] += v
        diff[R + 1] -= v  # safe because diff has length n+1

    # prefix to materialize
    arr = [0] * n
    run = 0
    for i in range(n):
        run += diff[i]
        arr[i] = run
    return arr


Let n = 8, all zeros initially.
Updates (inclusive ranges):

add +5 to [2, 5]

add -3 to [0, 3]

add +2 to [4, 7]

Step 1: start with diff = [0,0,0,0,0,0,0,0,0] (length n+1 = 9)


Apply update 1: [2,5] += 5

diff[2] += 5 → diff[2] = 5

diff[6] -= 5 → diff[6] = -5

diff now:
[0, 0, 5, 0, 0, 0, -5, 0, 0]

Apply update 2: [0,3] += (-3)

diff[0] += -3 → diff[0] = -3

diff[4] -= -3 → diff[4] = +3

diff now:
[-3, 0, 5, 0, 3, 0, -5, 0, 0]

Apply update 3: [4,7] += 2

diff[4] += 2 → diff[4] = 5

diff[8] -= 2 → diff[8] = -2

diff now:
[-3, 0, 5, 0, 5, 0, -5, 0, -2]

Step 2: prefix-sum to materialize the final array

run=0

i=0: run += -3 → -3

i=1: run += 0 → -3

i=2: run += 5 → 2

i=3: run += 0 → 2

i=4: run += 5 → 7

i=5: run += 0 → 7

i=6: run += -5 → 2

i=7: run += 0 → 2

Final arr = [-3, -3, 2, 2, 7, 7, 2, 2]



15) Character/feature prefix counts (strings & categories)


Build a prefix array where each position stores how many of each feature you’ve seen up to there.


from typing import List, Callable, Dict, Any

# ========== 1) LOWERCASE-ONLY (a..z) FAST PATH ==========

def build_prefix_counts_lower(s: str) -> List[List[int]]:
    """
    P[i][k] = count of letter (k=0..25 -> 'a'+k) in s[:i]
    Size: (len(s)+1) x 26
    """
    n = len(s)
    P = [[0]*26 for _ in range(n+1)]
    for i, ch in enumerate(s, 1):
        row = P[i]
        prev = P[i-1]
        # copy previous counts
        row[:] = prev
        # add current character
        k = ord(ch) - 97
        if 0 <= k < 26:  # ignore non-lowercase (optional)
            row[k] += 1
    return P

def count_char_in_range_lower(P: List[List[int]], L: int, R: int, ch: str) -> int:
    k = ord(ch) - 97
    return 0 if not (0 <= k < 26) else P[R+1][k] - P[L][k]

def freq_range_lower(P: List[List[int]], L: int, R: int) -> List[int]:
    return [P[R+1][k] - P[L][k] for k in range(26)]

def are_anagrams_lower(P: List[List[int]], L1: int, R1: int, L2: int, R2: int) -> bool:
    if (R1-L1) != (R2-L2):  # quick length check
        return False
    return freq_range_lower(P, L1, R1) == freq_range_lower(P, L2, R2)

def can_perm_palindrome_lower(P: List[List[int]], L: int, R: int) -> bool:
    # A substring can form a palindrome iff at most one char has an odd count
    odd = 0
    for k in range(26):
        if (P[R+1][k] - P[L][k]) & 1:
            odd += 1
            if odd > 1:
                return False
    return True


# ========== 2) GENERIC FEATURES (ANY BUCKETIZATION) ==========

def build_prefix_buckets(
    seq: List[Any],
    bucket_of: Callable[[Any], int],
    B: int
) -> List[List[int]]:
    """
    Generic prefix counts.
    - seq: sequence of items (chars, ints, tokens…)
    - bucket_of(x): maps item -> bucket index in [0..B-1]
    - returns P where P[i][b] = count of bucket b in seq[:i]
    """
    n = len(seq)
    P = [[0]*B for _ in range(n+1)]
    for i, x in enumerate(seq, 1):
        row, prev = P[i], P[i-1]
        row[:] = prev
        b = bucket_of(x)
        if 0 <= b < B:
            row[b] += 1
    return P

def count_bucket_in_range(P: List[List[int]], L: int, R: int, b: int) -> int:
    return P[R+1][b] - P[L][b]

def freq_range_buckets(P: List[List[int]], L: int, R: int) -> List[int]:
    B = len(P[0])
    return [P[R+1][b] - P[L][b] for b in range(B)]


# ========== 3) PARITY MASK TRICK (palindrome-permutation, super fast) ==========

def build_parity_mask_lower(s: str) -> List[int]:
    """
    M[i] = XOR parity mask of a..z for s[:i]
    Bit k toggles on each occurrence of chr(97+k).
    """
    n = len(s)
    M = [0]*(n+1)
    for i, ch in enumerate(s, 1):
        k = ord(ch) - 97
        m = M[i-1]
        if 0 <= k < 26:
            m ^= (1 << k)
        M[i] = m
    return M

def can_perm_palindrome_lower_mask(M: List[int], L: int, R: int) -> bool:
    mask = M[R+1] ^ M[L]            # parity of s[L..R]
    # <= 1 bit set (classic trick): x & (x-1) == 0
    return mask == 0 or (mask & (mask - 1)) == 0


# ========== 4) DEMO ==========

if __name__ == "__main__":
    s = "abacab"  # indices: 0 1 2 3 4 5
    P = build_prefix_counts_lower(s)

    # Count examples
    print("count('a', 1..4) =", count_char_in_range_lower(P, 1, 4, 'a'))  # "baca" -> 2
    print("count('b', 0..5) =", count_char_in_range_lower(P, 0, 5, 'b'))  # "abacab" -> 2

    # Anagram example: "aba"(0..2) vs "baa"(1..3) -> True
    print("anagrams?", are_anagrams_lower(P, 0, 2, 1, 3))

    # Palindrome-permutation check for "baca"(1..4): True (can form "abba")
    print("can perm palindrome? (1..4)", can_perm_palindrome_lower(P, 1, 4))

    # Parity mask version (same palindrome-permutation decision)
    M = build_parity_mask_lower(s)
    print("mask version:", can_perm_palindrome_lower_mask(M, 1, 4))

    # Generic buckets example: vowels vs consonants
    vowels = set("aeiou")
    def bucket_of_char(ch: str) -> int:
        if ch.isalpha():
            return 0 if ch.lower() in vowels else 1
        return 2  # bucket 2 for non-letters (if present)
    B = 3  # [vowel, consonant, other]
    P2 = build_prefix_buckets(list(s), bucket_of_char, B)
    L, R = 0, 5
    print("vowels in [0..5]:", count_bucket_in_range(P2, L, R, 0))
    print("consonants in [0..5]:", count_bucket_in_range(P2, L, R, 1))



How to identify which pattern applies (fast)

Exact sum K? → #2 (count) or #3 (longest).

Divisible / remainder? → #4 (mod trick).

Equal A/B? → #5 (recode to +1/−1).

XOR target? → #6 (prefix XOR).

Many range sums (no updates)? → #1 or #7.

Grid rectangles? → #8, #9.

Tree paths from root? → #10.

Balance point (left==right)? → #11.

Shortest subarray ≥ K with negatives? → #13 (deque).

Bulk range increments then finalize? → #14 (difference).

Substring letter counts? → #15 (prefix freq).













