class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # dp[x] - the longest ideal string length ended with chr(ord('a') + x)
        dp = [0] * 26

        # dp
        for ch in s:
            idx = ord(ch) - ord('a')
            maxi = 0
            for x in range(max(0, idx - k), min(25, idx + k) + 1):
                maxi = max(maxi, dp[x])
            dp[idx] = maxi + 1

        return max(dp)


s = "acfgbd"
k = 2

s = "abcd"
k = 3

s = "azazazazazaz"
k = 24

solution = Solution()
print(solution.longestIdealString(s, k))
