class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        # dp init
        M = len(mana)
        N = len(skill) + 1
        prev = [0] * N
        for y in range(1, N):
            prev[y] = skill[y - 1] * mana[0] + prev[y - 1]

        # dp transfer
        for x in range(1, M):
            dp = [0] * N
            # forward process
            for y in range(1, N):
                dp[y] = max(prev[y], dp[y - 1]) + skill[y - 1] * mana[x]
            # reverse process
            for y in range(N - 2, -1, -1):
                dp[y] = dp[y + 1] - skill[y] * mana[x]
            prev = dp
        ans = prev[N - 1]
        return ans


skill = [1,5,2,4]
mana = [5,1,4,2]

skill = [1, 1, 1]
mana = [1, 1, 1]

skill = [1,2,3,4]
mana = [1,2]

"""
from random import randint
skill = [randint(1, 5000) for _ in range(5000)]
mana = [randint(1, 5000) for _ in range(5000)]
print(skill)
print(mana)
"""

skill = [1]
mana = [49]

solution = Solution()
print(solution.minTime(skill, mana))
