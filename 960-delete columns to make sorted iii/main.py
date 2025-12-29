class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # pre-process
        M = len(strs)
        N = len(strs[0])

        cols = list()
        for y in range(N):
            col = ""
            for x in range(M):
                col += strs[x][y]
            cols.append(col)

        # helper function
        def ordered(col, col2):
            for x in range(M):
                if col[x] > col2[x]:
                    return False
            return True

        # process
        # dp init
        # dp[x] - the minimal deltions to make strs[:x+1] sorted
        dp = [1] * N

        # dp transfer
        # dp[x] - min(dp[y] + 1) if y <= x for all y before x
        for x in range(1, N):
            for y in range(x):
                if ordered(cols[y], cols[x]):
                    dp[x] = max(dp[x], dp[y] + 1)
        # print(dp)
        ans = N - max(dp)
        return ans


strs = ["babca","bbazb"]
strs = ["edcba"]
strs = ["ghi","def","abc"]
strs = ["aabbaa","baabab","aaabab"]

solution = Solution()
print(solution.minDeletionSize(strs))
