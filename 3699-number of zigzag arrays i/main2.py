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

        # dp_prev[y][t]
        dp_prev = [[0, 0] for _ in range(m)]

        # direct O(m) initialization for length = 2
        for y in range(m):
            dp_prev[y][1] = y  # increasing: x < y
            dp_prev[y][0] = m - 1 - y  # decreasing: x > y

        if n == 1:
            return m
        if n == 2:
            return sum(dp_prev[y][0] + dp_prev[y][1] for y in range(m)) % MODULO

        # dp for lengths 3 to n
        for _ in range(3, n + 1):
            dp_curr = [[0, 0] for _ in range(m)]

            # prefix sums (NO modulo here)
            pref_dec = [0] * (m + 1)
            pref_inc = [0] * (m + 1)

            for x in range(m):
                pref_dec[x + 1] = pref_dec[x] + dp_prev[x][0]
                pref_inc[x + 1] = pref_inc[x] + dp_prev[x][1]

            total_inc = pref_inc[m]  # store once

            # transitions
            for y in range(m):
                dp_curr[y][0] = (total_inc - pref_inc[y + 1]) % MODULO
                dp_curr[y][1] = pref_dec[y] % MODULO

            dp_prev = dp_curr

        # final sum
        ans = 0
        for y in range(m):
            ans += dp_prev[y][0] + dp_prev[y][1]

        return ans % MODULO


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