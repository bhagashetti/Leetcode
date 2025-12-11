When to use Two pointers

1) while dealing with linear structure ( Arrays , Strings , Linkedlist)
2) when we want to traverse from different directions with different speeds, compare two elements , partition
3) we can solve with O(n)

Two pointer patterns 
-----------------

1) 1️⃣ Opposite-Ends on Sorted Array (Pair / Area Problems)
🧩 Problem Statement Looks Like

“Given a sorted array, find two numbers whose sum equals target.”
“Find two elements whose sum is closest to target.”
“Given heights, find max water container.”

💡 Intuition

Sorted arrays make it easy to increase or decrease sums predictably.
Moving the left pointer → increases sum; moving right pointer → decreases sum.
We can “home in” on the target instead of checking all pairs.

🧠 Why Two Pointers Work

We maintain two indices, left and right, and adjust based on the relationship between nums[left] + nums[right] and the goal.
Each move removes impossible pairs.

🧩 Example

Two Sum II – Input Sorted Array (#167)

Left/right start at ends.

If sum too small → move left forward (need larger).

If sum too big → move right backward (need smaller).

2) 2️⃣ Fixed-and-Move (k-Sum / 3Sum / 4Sum)
🧩 Problem Statement Looks Like

“Find all unique triplets [a,b,c] where a+b+c = 0.”
“Find all quadruplets that sum to target.”

💡 Intuition

You can reduce k-Sum → (k-2)-Sum by fixing one element and using two pointers on the rest.
Sorting helps avoid duplicates and gives directionality.

🧠 Why Two Pointers Work

After fixing one element, the sub-problem becomes “find two numbers in sorted list whose sum = target.”
Two-pointer logic from pattern 1 fits perfectly.

🧩 Example

3Sum (#15)
Sort → Fix nums[i] → run left/right inside for the remaining sum.

3) 3️⃣ Sliding Window (Variable-Size Subarray / Substring)
🧩 Problem Statement Looks Like

“Find the length of the longest substring without repeating characters.”
“Find smallest subarray with sum ≥ K.”
“Find maximum average subarray of length K.”

💡 Intuition

You need a contiguous range that satisfies a property.
Move right to expand; move left to shrink when invalid.
Always maintain a valid window.

🧠 Why Two Pointers Work

left and right mark the window boundaries; both only move forward.
We maintain state (frequency map, sum, etc.) as we go.

🧩 Example

Longest Substring Without Repeating Characters (#3)
Use a set/map to track seen chars.
If duplicate → move left until window valid again.

4) 4️⃣ Fast–Slow Pointers (Linked List Problems)
🧩 Problem Statement Looks Like

“Detect if linked list has a cycle.”
“Find middle of linked list.”
“Remove nth node from end.”

💡 Intuition

We can’t jump backward in a linked list, but two pointers at different speeds let us measure relative distances.

🧠 Why Two Pointers Work

Fast pointer moves 2× speed of slow:

If cycle exists → fast laps slow → they meet.

For middle → when fast ends, slow at middle.

For nth-from-end → fast goes n ahead, then move both together.

🧩 Example

Linked List Cycle (#141)
fast = head.next.next, slow = head.next
→ if they ever meet → cycle.

5) 5️⃣ Dual Sequence Comparison / Merge
🧩 Problem Statement Looks Like

“Merge two sorted arrays.”
“Check if one string is a subsequence of another.”
“Find intersection of two sorted lists.”

💡 Intuition

Both lists are ordered — we can scan them together rather than restart each time.

🧠 Why Two Pointers Work

One pointer per list.
Advance the pointer with smaller element (or both if equal).
Each pointer moves only forward → O(n+m).

🧩 Example

Is Subsequence (#392)
Compare chars of s & t.
Advance j each time; advance i when match.
If i reaches end → true.

6) 6️⃣ In-Place Reordering / Partitioning
🧩 Problem Statement Looks Like

“Reverse an array/string.”
“Move all zeros to the end.”
“Sort colors (Dutch National Flag).”
“Reverse vowels in a string.”

💡 Intuition

You need to rearrange elements without extra space.
Two pointers can mark regions or swap boundaries.

🧠 Why Two Pointers Work

Use pointers that converge or partition zones:

Left/right swapping (reversal).

Read/write (compaction).

Low/mid/high (three-way partition).

🧩 Example

Move Zeroes (#283)
Read pointer scans; write pointer places non-zero.
After traversal, fill zeros.

7) 7️⃣ Interval Sweep (Two Sorted Interval Lists)
🧩 Problem Statement Looks Like

“Given two lists of closed intervals, return their intersection.”
“Merge meeting times.”

💡 Intuition

Both lists sorted by start time.
Overlap exists only between current intervals.

🧠 Why Two Pointers Work

Use i, j on each list.
Compute overlap.
Advance pointer with earlier end (it cannot overlap more later).

🧩 Example

Interval List Intersections (#986)
start = max(a[i].start, b[j].start)
end = min(a[i].end, b[j].end)
If start ≤ end → overlap.

8) 8️⃣ Palindrome / Mirror Comparison
🧩 Problem Statement Looks Like

“Check if a string is palindrome (ignore case & non-alphanumeric).”
“Determine if two halves of string are equal.”

💡 Intuition

Mirror elements from both sides should match; skip irrelevant chars.

🧠 Why Two Pointers Work

Start from both ends; move inward; skip invalids; compare at each step.

🧩 Example

Valid Palindrome (#125)
l++ and r-- while ignoring non-letters; compare lowercased chars.

9) 9️⃣ Deduplication / Overwrite (Fast–Slow in Arrays)
🧩 Problem Statement Looks Like

“Remove duplicates from sorted array.”
“Remove element equal to value.”

💡 Intuition

You’re “compressing” the array — keep unique values compacted at front.

🧠 Why Two Pointers Work

Slow pointer → write position for valid value.

Fast pointer → scans every element.
Each move either writes or skips.

🧩 Example

Remove Duplicates from Sorted Array (#26)
If nums[fast] ≠ nums[slow] → write, increment both.

10) 🔟 Special Variants — Mix Patterns

Some advanced problems combine techniques:

Problem Type	Combination	Example
Sliding window + counting	Maintain frequency + variable window	Minimum Window Substring (#76)
Opposite ends + condition check	Sorted + product/sign constraint	Squares of Sorted Array (#977)
Fast–slow + revers
