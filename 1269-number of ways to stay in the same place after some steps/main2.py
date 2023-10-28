class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        M = steps + 1
        N = min(steps, arrLen)

        # dp[x][y] - the number of ways to stay at y - offset position, after x steps
        old = [0] * N
        old[0] = 1

        for x in range(1, M):
            new = [0] * N
            for y in range(N):
                new[y] = old[y]
                if y > 0:
                    new[y] = (new[y] + old[y - 1]) % MODULO
                if y < N - 1:
                    new[y] = (new[y] + old[y + 1]) % MODULO
            old = new

        return old[0] % MODULO


steps = 3
arrLen = 2

steps = 2
arrLen = 4

steps = 4
arrLen = 2

solution = Solution()
print(solution.numWays(steps, arrLen))
