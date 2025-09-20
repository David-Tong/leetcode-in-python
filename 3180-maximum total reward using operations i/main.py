class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        # pre-process
        L = len(rewardValues)
        rewardValues = sorted(rewardValues)
        maxi = rewardValues[-1]

        # dp init
        prev = set()
        for rv in rewardValues:
            prev.add(rv)

        # shortcut
        if len(prev) == 1:
            return rewardValues[0]


        # dp transfer
        from bisect import bisect_right
        mini = min(prev)
        ans = 0
        while mini < maxi:
            curr = set()
            for reward in prev:
                idx = bisect_right(rewardValues, reward)
                if idx < L:
                    for x in range(idx, L):
                        curr.add(reward + rewardValues[x])
            ans = max(ans, max(curr))
            prev = curr
            mini = min(prev)
        return ans


rewardValues = [1,1,3,3]
rewardValues = [1,6,4,3,2]
rewardValues = [1]
rewardValues = [3, 3]
rewardValues = [2,9,18,17]

"""
from random import randint
rewardValues = [randint(1, 2000) for _ in range(2000)]
print(rewardValues)
"""

solution = Solution()
print(solution.maxTotalReward(rewardValues))
