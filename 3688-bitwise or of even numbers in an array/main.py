class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        idx = 0
        ans = 0
        while idx < L:
            if nums[idx] % 2 == 0:
                ans |= nums[idx]
            idx += 1
        return ans


nums = [1,2,3,4,5,6]
nums = [7,9,11]
nums = [1,8,16]

solution = Solution()
print(solution.evenNumberBitwiseORs(nums))
