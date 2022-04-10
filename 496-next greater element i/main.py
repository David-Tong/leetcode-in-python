class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # mark the index of nums1 in the array nums2
        indexes = {}
        for idx, num in enumerate(nums2):
            indexes[num] = idx

        # use monotonic stack to get the first greater number
        stack = []
        greaters = [-1] * len(nums2)
        for (idx, num) in enumerate(nums2):
            while len(stack) > 0 and nums2[stack[-1]] < num:
                item = stack.pop()
                greaters[item] = num
            stack.append(idx)

        ans = [0] * len(nums1)
        for idx, num in enumerate(nums1):
            ans[idx] = greaters[indexes[num]]

        return ans


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

solution = Solution()
print(solution.nextGreaterElement(nums1, nums2))
