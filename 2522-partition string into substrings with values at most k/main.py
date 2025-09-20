class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # dp init
        # dp[x] - the minimal number of substring in a good partition of s[ :x + 1]
        L = len(s)
        dp = [float("inf")] * L
        K = len(str(k))
        x = -1
        for x in range(min(L, K - 1)):
            dp[x] = 1
        if x + 1 < L:
            if int(s[:K]) <= k:
                dp[x + 1] = 1
        print(dp)

        # dp transfer
        # dp[x] - min(dp[x - k - 1], dp[x - k] if s[x - k: x + 1] <= k)
        for x in range(K - 1, L):
            dp[x] = min(dp[x], dp[x - (K - 1)] + 1)
            if x - K >= 0:
                print(s[x - K + 1: x + 1])
                if int(s[x - K  + 1: x + 1]) <= k:
                    dp[x] = min(dp[x], dp[x - K] + 1)

        ans = -1 if dp[L - 1] == float("inf") else dp[L - 1]
        return ans


s = "165462"
k = 60

s = "238182"
k = 5

s = "245678432"
k = 33

s = "1"
k = 1

s = "1762"
k = 593445230

solution = Solution()
print(solution.minimumPartition(s, k))
