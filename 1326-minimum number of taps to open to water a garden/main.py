class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        # min tap to water garden until points n
        dp = [float("inf")] * (n + 1)
        for idx, rng in enumerate(ranges):
            mini = float("inf")
            if idx - rng <= 0:
                mini = 0
            else:
                # look back
                for idx2 in range(max(0, idx - rng), idx):
                    mini = min(mini, dp[idx2])

            # look forward
            for idx2 in range(max(0, idx - rng), min(n, idx + rng) + 1):
                dp[idx2] = min(dp[idx2], mini + 1)

        return -1 if dp[n] == float("inf") else dp[n]


n = 5
ranges = [3,4,1,1,0,0]

n = 3
ranges = [0,0,0,0]

n = 8
ranges = [3,4,1,2,1,1,1,2,1]

n = 8
ranges = [4,0,0,0,4,0,0,0,4]

solution = Solution()
print(solution.minTaps(n, ranges))
