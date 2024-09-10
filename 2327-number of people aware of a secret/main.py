class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        # dp init
        # dp[x] - the number of people knows the secret of the x + 1 day
        dp = [0] * n
        dp[0] = 1

        # dp transfer
        for x in range(n):
            if forget > delay:
                start = min(x + delay, n)
                end = min(x + forget, n)
                for y in range(start, end):
                    dp[y] += dp[x]

        # post-process
        # print(dp)
        MODULO = 10 ** 9 + 7
        ans = 0
        for x in range(n - forget, n):
            ans = (ans + dp[x]) % MODULO
        return ans % MODULO


n = 6
delay = 2
forget = 4

n = 4
delay = 1
forget = 3

n = 1000
delay = 5
forget = 100

solution = Solution()
print(solution.peopleAwareOfSecret(n, delay, forget))
