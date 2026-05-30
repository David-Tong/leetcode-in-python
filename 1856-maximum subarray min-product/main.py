class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        MODULO = 10 ** 9 + 7

        # presums
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)

        # find the least right number larger than itself
        rights = [float("inf")] * L
        stack = list()
        idx = 0
        while idx < L:
            while stack and stack[-1][1] > nums[idx]:
                idx2, num2 = stack.pop()
                rights[idx2] = idx
            stack.append((idx, nums[idx]))
            idx += 1

        while stack:
            idx2, num2 = stack.pop()
            rights[idx2] = L

        # find the least left number larger than itself
        lefts = [float("-inf")] * L
        stack = list()
        idx = L - 1
        while idx >= 0:
            while stack and stack[-1][1] > nums[idx]:
                idx2, num2 = stack.pop()
                lefts[idx2] = idx
            stack.append((idx, nums[idx]))
            idx -= 1

        while stack:
            idx2, num2 = stack.pop()
            lefts[idx2] = -1

        # print(rights)
        # print(lefts)

        # process
        ans = 0
        idx = 0
        while idx < L:
            ans = max(ans, nums[idx] * (presums[rights[idx]] - presums[lefts[idx] + 1]))
            idx += 1
        ans = ans % MODULO
        return ans


nums = [1,2,3,2]
nums = [2,3,3,1,2]
nums = [3,1,5,6,4,2]

from random import randint
nums = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.maxSumMinProduct(nums))