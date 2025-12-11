class Solution:
    def nextGreaterElement(self, nums1, nums2) :

        stack = []
        d = {}
        n = len(nums2)
        for i in range(n):
            while stack and nums2[stack[-1]] < nums2[i]:
                d[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        n = len(nums1)
        result = []
        for i in range(n):
            result.append(d.get(nums1[i],-1))
        return result
