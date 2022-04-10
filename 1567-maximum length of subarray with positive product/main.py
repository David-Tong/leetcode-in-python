class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        positives = [0] * N
        negatives = [0] * N
        if nums[0] > 0:
            positives[0] = 1
        elif nums[0] < 0:
            negatives[0] = 1

        for x in range(1, N):
            if nums[x] > 0:
                positives[x] = positives[x-1] + 1
                if negatives[x-1] > 0:
                    negatives[x] = negatives[x-1] + 1
            elif nums[x] < 0:
                negatives[x] = positives[x - 1] + 1
                if negatives[x-1] > 0:
                    positives[x] = negatives[x-1] + 1

        return max(positives)


nums = [1, -2, -3, 4]
nums = [0, 1, -2, -3, -4]
nums = [-1, -2, -3, 0, 1]
nums = [-1]
nums = [1, 2, 0, -3, -6, -7, 2, 0, 9, 1]


solution = Solution()
print(solution.getMaxLen(nums))
