class Solution(object):
    def maxScore(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        # dp init
        # dp[x][y] - the max score after processing y elements in b[:x + 1]
        M = len(b)
        N = 4
        dp = [[float("-inf")] * N for _ in range(M)]
        dp[0][0] = a[0] * b[0]

        # dp transfer
        # dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - 1] + a[y] * b[x])
        for x in range(1, M):
            for y in range(N):
                if y > 0:
                    dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - 1] + a[y] * b[x])
                else:
                    dp[x][y] = max(dp[x - 1][y], a[y] * b[x])
        # print(dp)

        ans = float("-inf")
        for x in range(M):
            ans = max(ans, dp[x][N - 1])
        return ans


a = [3,2,5,6]
b = [2,-6,4,-5,-3,2,-7]

a = [-1,4,5,-2]
b = [-5,-1,-3,-2,-4]

a = [-1, 3, -6, -7]
b = [55, 43, -29, -45, 45, 87, 24, -55, -66, -67]

from random import randint
a = [randint(-10 ** 5, 10 ** 5) for _ in range(4)]
b = [randint(-10 ** 5, 10 ** 5) for _ in range(10 ** 5)]
print(a)
print(b)

solution = Solution()
print(solution.maxScore(a, b))
