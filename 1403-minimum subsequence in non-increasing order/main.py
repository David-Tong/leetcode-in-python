class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        nums = sorted(nums, reverse=True)
        total = sum(nums)

        # process
        part = 0
        ans = list()
        for num in nums:
            part += num
            total -= num
            ans.append(num)
            if part > total:
                return ans
        return ans


nums = [4,3,10,9,8]
nums = [4,4,7,6,7]

solution = Solution()
print(solution.minSubsequence(nums))
