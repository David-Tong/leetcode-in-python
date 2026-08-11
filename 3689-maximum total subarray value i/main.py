class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        maxi = max(nums)
        mini = min(nums)

        # process
        ans = (maxi - mini) * k
        return ans


nums = [1,3,2]
k = 2

nums = [4,2,5,1]
k = 3

from random import randint
nums = [randint(1,10 ** 9) for _ in range(5 * 10 ** 4)]
k = 10 ** 5
print(nums)

solution = Solution()
print(solution.maxTotalValue(nums, k))