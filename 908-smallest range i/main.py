class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = max(nums)
        mini = min(nums)

        if maxi - k > mini + k:
            return (maxi - mini) - 2 * k
        else:
            return 0


nums = [1]
k = 0

nums = [0,10]
k = 2

nums = [1,3,6]
k = 3

solution = Solution()
print(solution.smallestRangeI(nums, k))