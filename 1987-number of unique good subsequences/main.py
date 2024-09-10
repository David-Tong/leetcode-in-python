class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        MODULO = 10**9 + 7
        # dp init
        # dp[0] - number of unique good subsequence ended with 0, but no leading 0
        # dp[1] - number of unique good subsequence ended with 1
        dp = [0] * 2

        # dp transfer
        zero = 0
        for b in binary:
            if b == "0":
                zero = 1
                dp[0] = (dp[0] + dp[1]) % MODULO
            elif b == "1":
                dp[1] = (1 + dp[0] + dp[1]) % MODULO

        ans = (sum(dp) + zero) % MODULO
        return ans


binary = "001"
binary = "000"
binary = "11"
binary = "101"
binary = "1110101010110111"

solution = Solution()
print(solution.numberOfUniqueGoodSubsequences(binary))
