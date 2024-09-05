class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        sorts = set()
        for num in nums:
            sorts.add(num)
        sorts = sorted(list(sorts))

        N = len(nums)
        S = len(sorts)

        def canContinue(target):
            if target == N - 1:
                return True

            for x in range(S):
                if x + N - 1 - target < S:
                    if sorts[x + N - 1 - target] - sorts[x] <= N - 1:
                        return True
            return False

        left = 0
        right = N - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if canContinue(middle):
                right = middle
            else:
                left = middle + 1

        if canContinue(left):
            return left
        else:
            return right


nums = [4,2,5,3]
nums = [1,2,3,5,6]
nums = [1,2,3,6,7]
nums = [1,10,100,1000]
nums = [2,2,2,2,2]
nums = [2,3,2,2,2]

solution = Solution()
print(solution.minOperations(nums))
