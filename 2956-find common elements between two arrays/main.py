class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # pre-process
        set1, set2 = set(nums1), set(nums2)

        # process
        count1 = 0
        for num1 in nums1:
            if num1 in set2:
                count1 += 1

        count2 = 0
        for num2 in nums2:
            if num2 in set1:
                count2 += 1

        ans = [count1, count2]
        return ans


nums1 = [2,3,2]
nums2 = [1,2]

nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]

nums1 = [3,4,2,3]
nums2 = [1,5]

solution = Solution()
print(solution.findIntersectionValues(nums1, nums2))
