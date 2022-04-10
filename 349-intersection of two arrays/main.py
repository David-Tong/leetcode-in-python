class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums1:
            dicts[num] += 1

        intersection = set()
        for num in nums2:
            if num in dicts:
                intersection.add(num)
        return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

solution = Solution()
print(solution.intersection(nums1, nums2))
