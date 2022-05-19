class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        N = len(envelopes)
        if N == 0:
            return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        # dp[x] - the minimal value in the end for a strictly increasing sequnce with the length of x in envelopes
        dp = []
        dp.append(envelopes[0][1])

        for x in range(1, N):
            num = envelopes[x][1]
            if num > dp[-1]:
                dp.append(num)
            else:
                from bisect import bisect_left
                idx = bisect_left(dp, num)
                dp[idx] = num

        return len(dp)


envelopes = [[5,4],[6,4],[6,7],[2,3]]
#envelopes = [[1,1],[1,1],[1,1]]
#envelopes = [[5,4],[3,9],[6,7],[2,3]]
envelopes = [[4,5],[4,6],[6,7],[7,7],[2,3],[1,1],[1,1]]
envelopes = [[4,5],[4,6],[6,7],[7,7],[2,3],[1,1],[1,3],[1,1],[2,7],[3,15]]

solution = Solution()
print(solution.maxEnvelopes(envelopes))
