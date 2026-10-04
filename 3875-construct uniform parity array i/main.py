class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        return True


nums1 = [2,3]
nums1 = [4,6]

from random import randint
nums1 = list(set(randint(1, 100) for _ in range(100)))
print(nums1)

solution = Solution()
print(solution.uniformArray(nums1))
