class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        total = sum(nums)

        total2 = 0
        for num in nums:
            while num:
                total2 += num % 10
                num = num // 10

        # process
        ans = total - total2
        return ans


nums = [1,15,6,3]
nums = [1,2,3,4]

solution = Solution()
print(solution.differenceOfSum(nums))
