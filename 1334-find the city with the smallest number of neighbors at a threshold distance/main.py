class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # dp
        # dp[x][y] - minimal distance between city x and y
        dp = [[float("inf")] * n for _ in range(n)]
        for x in range(n):
            dp[x][x] = 0


        # pre-process
        for edge in edges:
            x, y, distance = edge
            dp[x][y] = distance
            dp[y][x] = distance

        # dp transfer
        for c in range(n):
            for x in range(n):
                for y in range(n):
                    dp[x][y] = min(dp[x][y], dp[x][c] + dp[c][y])

        # post-process
        reachables = [-1] * n
        for x in range(n):
            for y in range(n):
                if dp[x][y] <= distanceThreshold:
                    reachables[x] += 1

        mini = min(reachables)
        ans = -1
        for x in range(n):
            if reachables[x] == mini:
                ans = x
        return ans


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

solution = Solution()
print(solution.findTheCity(n, edges, distanceThreshold))
