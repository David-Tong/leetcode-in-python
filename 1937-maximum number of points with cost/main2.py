class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # init dp
        # dp[x][y] - maximum number of points to move to points[x][y]
        M = len(points)
        N = len(points[0])
        dp = [[0] * N for _ in range(M)]
        for y in range(N):
            dp[0][y] = points[0][y]

        # transfer dp
        for x in range(1, M):
            for y in range(N):
                for z in range(N):
                    dp[x][y] = max(dp[x][y], dp[x - 1][z] + points[x][y] - abs(y - z))

        # post-process
        # print(dp)
        ans = max(dp[M - 1])
        return ans


points = [[1,2,3],[1,5,1],[3,1,1]]
points = [[1,5],[2,3],[4,2]]
points = [[0] * 1000 for _ in range(100)]

solution = Solution()
print(solution.maxPoints(points))
