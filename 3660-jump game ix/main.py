class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # search maximum number from the left
        left_maxis = [0] * L
        left_maxi = float('-inf')
        idx = 0
        while idx < L:
            left_maxi = max(left_maxi, nums[idx])
            left_maxis[idx] = left_maxi
            idx += 1
        # print(left_maxis)

        # search minimum number from the right
        right_minis = [0] * L
        right_mini = float('inf')
        idx = L - 1
        while idx >= 0:
            right_mini = min(right_mini, nums[idx])
            right_minis[idx] = right_mini
            idx -= 1
        # print(right_minis)

        # process
        # left_maxis[x] <= right_minis[x + 1], the maximum value is in the nums[:x + 1]
        # left_maxis[x] > right_minis[x + 1], the maximum value is the one x + 1 has
        ans = [0] * L
        ans[L - 1] = left_maxis[L- 1]
        idx = L - 2
        while idx >= 0:
            if left_maxis[idx] > right_minis[idx + 1]:
                ans[idx] = ans[idx + 1]
            else:
                ans[idx] = left_maxis[idx]
            idx -= 1
        return ans


nums = [2,1,3]
nums = [2,3,1]
nums = [30,21,5,35,24]
nums = [9,30,16,6,36,9]
nums = [1,1,1,1,1]

from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.maxValue(nums))
