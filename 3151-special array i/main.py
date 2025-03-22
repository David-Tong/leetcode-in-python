class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)

        # process
        parity = nums[0] % 2
        for x in range(1, L):
            if nums[x] % 2 != 1 - parity:
                return False
            parity = 1 - parity
        return True


nums = [1]
nums = [2,1,4]
nums = [4,3,1,6]

solution = Solution()
print(solution.isArraySpecial(nums))
