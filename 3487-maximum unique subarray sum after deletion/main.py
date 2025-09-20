class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        s = set()
        for num in nums:
            s.add(num)

        # process
        ans = 0
        has = False
        negative = float("-inf")
        for num in s:
            if num >= 0:
                has = True
                ans += num
            else:
                negative = max(negative, num)
        return ans if has else negative


nums = [1,2,3,4,5]
nums = [1,1,0,1,1]
nums = [1,2,-1,-2,1,0,-1]
nums = [-100]
nums = [-17,-15]

solution = Solution()
print(solution.maxSum(nums))
