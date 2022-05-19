class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        N = len(envelopes)
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        dp = [1] * N
        for x in range(1, N):
            for y in range(0, x):
                if envelopes[x][1] > envelopes[y][1]:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp)


envelopes = [[5,4],[6,4],[6,7],[2,3]]
#envelopes = [[1,1],[1,1],[1,1]]
#envelopes = [[5,4],[3,9],[6,7],[2,3]]
envelopes = [[4,5],[4,6],[6,7],[7,7],[2,3],[1,1],[1,1]]
envelopes = [[4,5],[4,6],[6,7],[7,7],[2,3],[1,1],[1,3],[1,1],[2,7],[3,15]]

solution = Solution()
print(solution.maxEnvelopes(envelopes))
