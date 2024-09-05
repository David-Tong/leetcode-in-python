class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1 & set2

        ans1 = list()
        for num in set1:
            if num not in intersection:
                ans1.append(num)

        ans2 = list()
        for num in set2:
            if num not in intersection:
                ans2.append(num)

        return [ans1, ans2]


nums1 = [1,2,3]
nums2 = [2,4,6]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

nums1 = [1]
nums2 = [1]

solution = Solution()
print(solution.findDifference(nums1, nums2))
