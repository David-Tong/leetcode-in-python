class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        from collections import defaultdict
        diffs = defaultdict(int)

        for num in nums:
            diff = num - int(str(num)[::-1])
            diffs[diff] += 1

        # process
        ans = 0
        for diff in diffs:
            ans += (diffs[diff] * (diffs[diff] - 1) // 2) %MODULO
        return ans % MODULO


nums = [42,11,1,97]
nums = [13,10,35,24,76]
nums = [13,35,31,53]
nums = [0,11,22,33,55]

solution = Solution()
print(solution.countNicePairs(nums))
