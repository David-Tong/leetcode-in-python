class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for pw in power:
            dicts[pw] += 1
        processed = sorted(dicts.keys())
        # print(dicts)
        # print(processed)

        # dp init
        # dp[x] - maximum total damage for processed[:x + 1]
        L = len(processed)
        dp = [0] * L
        dp[0] = processed[0] * dicts[processed[0]]

        # dp transfer
        for x in range(1, L):
            dp[x] = max(dp[x - 1], processed[x] * dicts[processed[x]])
            idx = x - 1
            while idx >= 0 and processed[x] - processed[idx] <= 2:
                idx -= 1
            if idx >= 0:
                dp[x] = max(dp[x], dp[idx] + processed[x] * dicts[processed[x]])
        # print(dp)

        ans = dp[L - 1]
        return ans


power = [1,1,3,4]
power = [7,1,6,6]
power = [2,1,1,1,1,1,1,1,1,1,2,3,3,1,1,1,1,1,1,1,1,1,1,1,4,5,5,6,1,1,1,1,1]

"""
from random import randint
power = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(power)
"""

solution = Solution()
print(solution.maximumTotalDamage(power))
