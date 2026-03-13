class Solution(object):
    def maxRemovals(self, source, pattern, targetIndices):
        """
        :type source: str
        :type pattern: str
        :type targetIndices: List[int]
        :rtype: int
        """
        # pre-process
        M = len(source)
        N = len(pattern)
        removable = set(targetIndices)

        # process
        # dp init
        # dp[x][y] = the maximum removals from source[:x] to match pattern[:y]
        dp = [[float("-inf")] * (N + 1) for _ in range(M + 1)]
        removal = 0
        for x in range(M + 1):
            dp[x][0] = removal
            if x in removable:
                removal += 1

        # dp transfer
        # dp[x][y] = max(
        #   dp[x - 1][y - 1] if source[x - 1] == patten[y - 1]
        #   dp[x - 1][y] if x - 1 not in target indices
        #   dp[x - 1][y] + 1 if x - 1 in target indices
        # )
        for x in range(M):
            for y in range(N):
                # case 1
                if source[x] == pattern[y]:
                    dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y])
                # case 2
                if x in removable:
                    dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y + 1] + 1)
                else:
                    dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y + 1])
        # print(dp)
        ans = dp[M][N]
        return ans


source = "abbaa"
pattern = "aba"
targetIndices = [0,1,2]

source = "bcda"
pattern = "d"
targetIndices = [0,3]

source = "dda"
pattern = "dda"
targetIndices = [0,1,2]

source = "yeyeykyded"
pattern = "yeyyd"
targetIndices = [0,2,3,4]

solution = Solution()
print(solution.maxRemovals(source, pattern, targetIndices))
