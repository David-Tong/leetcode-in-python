class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(list)

        # mark start index for every number
        for idx, num1 in enumerate(nums1):
            if num1 not in nums1:
                dicts[num1] = list()
            dicts[num1].append(idx)

        # search for
        ans = 0
        for start2, num2 in enumerate(nums2):
            for start1 in dicts[num2]:
                idx = 0
                while start1 + idx < len(nums1) and \
                        start2 + idx < len(nums2) and \
                        nums1[start1 + idx] == nums2[start2 + idx]:
                    idx += 1
                ans = max(ans, idx)
        return ans


nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]

solution = Solution()
print(solution.findLength(nums1, nums2))
