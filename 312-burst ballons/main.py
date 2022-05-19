class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        nums = nums + [1]
        # dp[x][y] - max coin to burst balloons between nums[x:y+1]
        dp = [[0] * N for _ in range(N)]

        for x in range(N - 1, -1, -1):
            dp[x][x] = nums[x-1] * nums[x] * nums[x+1]
            for y in range(x + 1, N):
                for z in range(x, y + 1):
                    if z > 0 and z < N - 1:
                        dp[x][y] = max(dp[x][y], dp[x][z-1] + nums[x-1] * nums[z] * nums[y+1] + dp[z+1][y])
                    elif z > 0:
                        dp[x][y] = max(dp[x][y], dp[x][z - 1] + nums[x - 1] * nums[z] * nums[y + 1])
                    elif z < N - 1:
                        dp[x][y] = max(dp[x][y], nums[x - 1] * nums[z] * nums[y + 1] + dp[z + 1][y])

        return dp[0][N-1]


nums = [3,1,5,8]
#nums = [3,1,5]
nums = [1,5]
#nums = [1,4,5,6,9,12,3]

solution = Solution()
print(solution.maxCoins(nums))
