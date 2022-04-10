class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        from math import log, pow, floor
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for x in range(2, n + 1):
            base2 = floor(log(x) / log(2))
            pow2 = int(pow(2, base2))
            dp[x] = 1 + dp[x - pow2]

        return dp


n = 5

solution = Solution()
print(solution.countBits(n))
