class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pre-process
        pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

        # dp[x] - the sequence with length x ended with right dp[x]
        dp = list()

        from bisect import bisect_left
        for pair in pairs:
            idx = bisect_left(dp, pair[0])
            if idx >= len(dp):
                dp.append(pair[1])
            else:
                dp[idx] = min(dp[idx], pair[1])

        return len(dp)


pairs = [[1,2],[2,3],[3,4]]
pairs = [[1,2],[7,8],[4,5]]
pairs = [[1,2],[2,3],[2,4]]
pairs = [[1,100],[1,2],[3,4],[5,6]]
pairs = [[1,2]]

solution = Solution()
print(solution.findLongestChain(pairs))
