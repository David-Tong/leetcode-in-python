class Solution(object):
    def minCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num1 in nums1:
            dicts[num1] += 1

        for num2 in nums2:
            dicts[num2] -= 1

        # process
        ans = 0
        for num in dicts:
            if abs(dicts[num]) % 2 != 0:
                return -1
            ans += abs(dicts[num])
        ans /= 4
        return ans


nums1 = [10,20]
nums2 = [20,10]

nums1 = [10,10]
nums2 = [20,20]

nums1 = [10,20]
nums2 = [30,40]

from random import choice
nums = [1,2,3,4]
nums1 = [choice(nums) for _ in range(8 * 10 ** 4)]
nums2 = [choice(nums) for _ in range(8 * 10 ** 4)]
print(nums1)
print(nums2)

solution = Solution()
print(solution.minCost(nums1, nums2))
