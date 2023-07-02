class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        N = len(nums)

        import sys
        sys.setrecursionlimit(N + 10)

        # two sequences dp
        # dp[x][y] - the number of ways to create a sequence with x + y elements
        #            but keep x, y element previous order
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = 1

        for x in range(N + 1):
            for y in range(N + 1):
                if x > 0 and y > 0:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
                elif x > 0:
                    dp[x][y] = dp[x - 1][y]
                elif y > 0:
                    dp[x][y] = dp[x][y - 1]

        def findWays(nums):
            N = len(nums)
            if N < 3:
                return 1

            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return findWays(left) * findWays(right) * dp[len(left)][len(right)] % MODULO

        return (findWays(nums) - 1) % MODULO


nums = [2,1,3]
nums = [3,4,5,1,2]
nums = [1,2,3]
nums = [8,4,2,6,1,3,5,7,12,10,14,9,11,13,15]
nums = [4,2,6,1,3,5,7]
nums = [1]
nums = [10,8,6,4,2,1,3,7,5,9]
nums = [13,15,3,5,10,2,12,8,7,4,6,1,14,9,11]
nums = [_ for _ in range(1, 2000)]

solution = Solution()
print(solution.numOfWays(nums))
