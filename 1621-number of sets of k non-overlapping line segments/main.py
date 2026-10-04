class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        # process
        # dp init
        # dp[k][x] - number of sets of k + 1 non-overlapping line segments, ended with xth point
        dp = [0] * n
        for x in range(n):
            dp[x] = x

        # dp transfer
        for z in range(1, k):
            # presum
            presum = [0] * (n + 1)
            presum2 = [0] * (n + 1)

            for x in range(n):
                presum[x + 1] = (presum[x] + dp[x]) % MODULO
                presum2[x + 1] = (presum2[x] + dp[x] * x) % MODULO

            new_dp = [0] * n
            # dp[z][x] only valid for x >= z
            for x in range(z, n):
                left = z - 1
                right = x - 1
                # dp[z][x] = sum(dp[z-1][y] * (x - y))
                # dp[z][x] = x * sum(dp[z-1][y] - y * sum(dp[z-1][y])
                sum_dp = (presum[right + 1] - presum[left]) % MODULO
                sum_idp = (presum2[right + 1] - presum2[left]) % MODULO
                new_dp[x] = (x * sum_dp - sum_idp) % MODULO

            dp = new_dp

        # print(dp)
        ans = sum(dp) % MODULO
        return ans


n = 4
k = 2

n = 3
k = 1

n = 30
k = 7

solution = Solution()
print(solution.numberOfSets(n, k))
