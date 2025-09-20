class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        # pre-process
        # the max reward <= 2 * max(rewardValues) - 1
        L = len(rewardValues)

        rewardValues = sorted(rewardValues)
        if L > 1 and rewardValues[-2] == rewardValues[-1] - 1:
            return 2 * rewardValues[-1] - 1

        # process
        # dp init
        # dp[x][y] - whether we can get the total reward y with the rewardValues[:x]
        # we may remove the dimension of x since it only depends on x - 1
        # using bitset
        dp = 1

        # dp transfer
        # dp[y] = dp[y] | dp[y - value]
        for rewardValue in rewardValues:
            # dp & ((1 << rewardValue) - 1) - clean up all bits higher or equal to rewardValue
            dp |= (dp & ((1 << rewardValue) - 1)) << rewardValue
        return dp.bit_length() - 1


rewardValues = [1,1,3,3]
rewardValues = [1,6,4,3,2]

solution = Solution()
print(solution.maxTotalReward(rewardValues))

