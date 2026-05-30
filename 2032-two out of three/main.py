class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(lambda: [0, 0, 0])

        for idx, nums in enumerate([nums1, nums2, nums3]):
            for num in nums:
                dicts[num][idx] = 1

        # process
        ans = list()
        for num in dicts:
            if sum(dicts[num]) >= 2:
                ans.append(num)
        return ans


nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]

solution = Solution()
print(solution.twoOutOfThree(nums1, nums2, nums3))
