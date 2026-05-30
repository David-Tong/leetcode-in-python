class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        # helper function
        def addUp(num):
            num = str(num)
            res = 0
            for ch in num:
                try:
                    res += int(ch)
                except ValueError:
                    return 0
            return res

        # process
        ans = float("inf")
        for num in nums:
            ans = min(ans, addUp(num))
        return ans


nums = [10,12,13,14]
nums = [1,2,3,4]
nums = [999,19,199]

solution = Solution()
print(solution.minElement(nums))
