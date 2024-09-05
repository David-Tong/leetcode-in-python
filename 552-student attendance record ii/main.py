class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # modulo
        MODULO = 10 ** 9 + 7

        # dp[0] - P or L and not ended with L   x3
        # dp[1] - P or L and ended with only one L  x3
        # dp[2] - P or L and ended with two continuous L    x2 not append L
        # dp[3] - P or L with one A and not ended with L    x2 not append A
        # dp[4] - P or L with one A and ended with only one L   x2 not append A
        # dp[5] - P or L with one A and ended with two continuous L x1 not append A or L
        # x13

        # init
        prev = [0] * 6
        prev[0] = 1
        prev[1] = 1
        prev[2] = 0
        prev[3] = 1
        prev[4] = 0
        prev[5] = 0

        # dp transfer
        if n == 1:
            ans = sum(prev)
        else:
            for x in range(1, n):
                dp = [0] * 6
                dp[0] = (prev[0] + prev[1] + prev[2]) % MODULO
                dp[1] = prev[0] % MODULO
                dp[2] = prev[1] % MODULO
                dp[3] = (prev[0] + prev[1] + prev[2] + prev[3] + prev[4] + prev[5]) % MODULO
                dp[4] = prev[3] % MODULO
                dp[5] = prev[4] % MODULO
                # print(dp)
                prev = dp

            ans = sum(dp)
        return ans % MODULO


n = 2
n = 3
n = 4
n = 88888

solution = Solution()
print(solution.checkRecord(n))
