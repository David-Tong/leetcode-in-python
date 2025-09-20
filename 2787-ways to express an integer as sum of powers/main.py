class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = int(n ** (1.0 / x) + 1)

        powers = list()
        for num in range(1, L + 1):
            powers.append(num ** x)
        # print(powers)

        # process
        # dp backpack
        # dp init
        # dp[x] - the ways to express an integer as sum of powers
        dp = [0] * (n + 1)
        dp[0] = 1

        # dp transfer
        for power in powers:
            for num in range(n, -1, -1):
                if num - power >= 0:
                    dp[num] = (dp[num] + dp[num - power]) % MODULO
        # print(dp)
        ans = dp[n]
        return ans


n = 10
x = 2

n = 4
x = 1

n = 160
x = 3

n = 300
x = 1

n = 300
x = 5

n = 49
x = 2

solution = Solution()
print(solution.numberOfWays(n, x))
