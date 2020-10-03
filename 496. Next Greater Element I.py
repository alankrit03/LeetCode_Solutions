class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        result = {}
        stack = []
        for i in range(n2):
            while stack and nums2[stack[-1]] < nums2[i]:
                result[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        else:
            while stack:
                result[nums2[stack.pop()]] = -1

        # print(result)
        ans = [-1] * n1

        for i in range(n1):
            ans[i] = result[nums1[i]]

        return ans