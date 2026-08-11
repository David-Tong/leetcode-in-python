class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        # process
        MODULO = 10 ** 9 + 7
        m = r - l + 1

        # dp[i][y][t] but we only keep dp for previous step
        dp_prev = [[0, 0] for _ in range(m)]

        # initialize for length = 2
        for a in range(m):
            for b in range(m):
                if a == b:
                    continue
                if b > a:
                    dp_prev[b][1] += 1
                else:
                    dp_prev[b][0] += 1

        if n == 1:
            return m
        if n == 2:
            return sum(dp_prev[y][0] + dp_prev[y][1] for y in range(m)) % MODULO

        # iterate for lengths 3..n
        for _ in range(3, n + 1):
            dp_curr = [[0, 0] for _ in range(m)]

            # prefix sums for dp_prev[*][0] and dp_prev[*][1]
            pref_dec = [0] * (m + 1)
            pref_inc = [0] * (m + 1)

            for i in range(m):
                pref_dec[i + 1] = (pref_dec[i] + dp_prev[i][0]) % MODULO
                pref_inc[i + 1] = (pref_inc[i] + dp_prev[i][1]) % MODULO

            # compute dp_curr
            for y in range(m):
                # decreasing trend: previous must be > y
                dp_curr[y][0] = (pref_inc[m] - pref_inc[y + 1]) % MODULO

                # increasing trend: previous must be < y
                dp_curr[y][1] = pref_dec[y] % MODULO

            dp_prev = dp_curr

        # sum all dp[n][y][*]
        ans = 0
        for y in range(m):
            ans = (ans + dp_prev[y][0] + dp_prev[y][1]) % MODULO

        return ans


n = 3
l = 4
r = 5

n = 3
l = 1
r = 3

n = 2000
l = 1
r = 2000

n = 238
l = 358
r = 1819

solution = Solution()
print(solution.zigZagArrays(n, l, r))
