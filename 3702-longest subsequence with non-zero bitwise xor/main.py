class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = L
        xors = 0
        zeros = True
        for num in nums:
            if num != 0:
                zeros = False
            xors ^= num
        if zeros:
            return 0
        if xors == 0:
            ans -= 1
        return ans


nums = [1,2,3]
nums = [2,3,4]
nums = [0,1,2,3,0,0]
nums = [0,0,1,2,3,0]
nums = [0,2,3,4,0,0]

from random import randint
nums = [randint(0, 10 ** 2) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.longestSubsequence(nums))
