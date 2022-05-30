class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def countZerosAndOnes(str):
            zeros = 0
            ones = 0
            for digit in str:
                if digit == "0":
                    zeros += 1
                elif digit == "1":
                    ones += 1
            return zeros, ones

        I = len(strs) + 1
        M = m + 1
        N = n + 1
        # dp[i][x][y] - max number of subset after checking the first ith str, with m zeros and n ones
        dp = [[[0] * N for _ in range(M)] for _ in range(I)]

        for x in range(I):
            if x == 0:
                continue
            else:
                zeros, ones = countZerosAndOnes(strs[x - 1])
                for y in range(M):
                    for z in range(N):
                        if y < zeros or z < ones:
                            dp[x][y][z] = dp[x - 1][y][z]
                        else:
                            dp[x][y][z] = max(dp[x - 1][y][z], dp[x - 1][y - zeros][z - ones] + 1)
        return dp[I - 1][M - 1][N - 1]


strs = ["10","0001","111001","1","0"]
m = 5
n = 3

strs = ["10","0","1"]
m = 1
n = 1

strs = ["0","1101","01","00111","1","10010","0","0","00","1","11","0011"]
m = 63
n = 36

solution = Solution()
print(solution.findMaxForm(strs, m, n))
