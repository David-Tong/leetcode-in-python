class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        dp.append([triangle[0][0]])
        for row in triangle[1:]:
            dp.append([0] * len(row))

        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    dp[row][col] = dp[row - 1][col] + triangle[row][col]
                elif col > 0 and col < len(triangle[row]) - 1:
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
                else:
                    dp[row][col] = dp[row - 1][col - 1] + triangle[row][col]
        return min(dp[len(triangle) - 1])


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]

solution = Solution()
print(solution.minimumTotal(triangle))
