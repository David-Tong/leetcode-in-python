class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        total = sum(nums)
        prefix = 0

        mini = float("inf")
        for idx, num in enumerate(nums):
            prefix += num
            if idx == L - 1:
                result = abs(prefix // (idx + 1))
            else:
                suffix = total - prefix
                result = abs(prefix // (idx + 1) - suffix // (L - 1 - idx))
            if result < mini:
                mini = result
                ans = idx
        return ans


nums = [2,5,3,9,5,3]
nums = [0]

solution = Solution()
print(solution.minimumAverageDifference(nums))
