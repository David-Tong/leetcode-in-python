class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums) + 1
        digits = [0] * N
        digits[0] = -1
        for num in nums:
            digits[num] = num

        for x in range(N):
            if digits[x] != x:
                return x


nums = [3, 0, 1]
nums = [0, 1]
nums = [9,6,4,2,3,5,7,0,1]
nums = [9,6,4,2,3,5,7,8,1]

solution = Solution()
print(solution.missingNumber(nums))
