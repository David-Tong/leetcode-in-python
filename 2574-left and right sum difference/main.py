class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        left_sums = list()
        left_sums.append(0)
        idx = 1
        while idx < L:
            left_sums.append(left_sums[-1] + nums[idx - 1])
            idx += 1
        # print(left_sums)

        right_sums = list()
        right_sums.append(0)
        idx = L - 2
        while idx >= 0:
            right_sums.append(right_sums[-1] + nums[idx + 1])
            idx -= 1
        right_sums = right_sums[::-1]
        # print(right_sums)

        # process
        ans = list()
        idx = 0
        while idx < L:
            ans.append(abs(left_sums[idx] - right_sums[idx]))
            idx += 1
        return ans


nums = [10,4,8,3]
nums = [1]

solution = Solution()
print(solution.leftRightDifference(nums))
