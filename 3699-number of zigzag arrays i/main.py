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

        # dp init
        dec_prev = [0] * m
        inc_prev = [0] * m

        # direct initialization for length = 2
        for y in range(m):
            inc_prev[y] = y  # x < y
            dec_prev[y] = m - 1 - y  # x > y

        if n == 1:
            return m
        if n == 2:
            return (sum(dec_prev) + sum(inc_prev)) % MODULO

        # dp transfer
        # dp for lengths 3 to n
        for _ in range(3, n + 1):
            dec_curr = [0] * m
            inc_curr = [0] * m

            # prefix sums (no modulo here)
            presums_dec = [0] * (m + 1)
            presums_inc = [0] * (m + 1)

            for x in range(m):
                presums_dec[x + 1] = presums_dec[x] + dec_prev[x]
                presums_inc[x + 1] = presums_inc[x] + inc_prev[x]

            total_inc = presums_inc[m]

            # transitions
            for y in range(m):
                dec_curr[y] = total_inc - presums_inc[y + 1]  # decreasing
                inc_curr[y] = presums_dec[y]  # increasing

            # apply modulo once per layer
            for x in range(m):
                dec_curr[x] %= MODULO
                inc_curr[x] %= MODULO

            dec_prev = dec_curr
            inc_prev = inc_curr

        ans = (sum(dec_prev) + sum(inc_prev)) % MODULO
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