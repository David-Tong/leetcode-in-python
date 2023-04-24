class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        from math import log
        M = int(log(k, 10))
        N = len(s)

        # check if number is valid
        def validNumber(number):
            if len(number) == 0 or number[0] == '0':
                return False
            number = long(number)
            if number > k:
                return False
            return True

        # dp[x] - the number of the possible arrays that can be printed as s[:x]
        dp = [0] * (N + 1)
        dp[0] = 1

        for x in range(1, N + 1):
            lower = max(0, x - M - 1)
            for y in range(lower, x):
                number = s[y:x]
                if validNumber(number):
                    dp[x] += dp[y]
        return dp[N] % MODULO


s = "1000"
k = 10000

s = "1000"
k = 10

s = "1317"
k = 2000

s = "13127648235328957092821948239578234590129748257801848357"
k = 88888888

s = "9"
k = 1

solution = Solution()
print(solution.numberOfArrays(s, k))
