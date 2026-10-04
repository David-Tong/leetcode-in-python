class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        def getDigitSum(num):
            res = 0
            for digit in str(num):
                res += int(digit)
            return res

        # process
        idx = 0
        while idx < L:
            if idx == getDigitSum(nums[idx]):
                return idx
            idx += 1
        return -1


nums = [1,3,2]
nums = [1,10,11]
nums = [1,2,3]

solution = Solution()
print(solution.smallestIndex(nums))
