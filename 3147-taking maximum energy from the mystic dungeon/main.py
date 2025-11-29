class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        # pre-proess
        L = len(energy)
        maxis = [0] * k

        # process
        ans = float("-inf")
        idx = L - 1
        while idx >= 0:
            mod = idx % k
            maxis[mod] += energy[idx]
            ans = max(ans, maxis[mod])
            idx -= 1
        return ans


energy = [5,2,-10,-5,1]
k = 3

energy = [-2,-3,-1]
k = 2

from random import randint
energy = [randint(-1000, 1000) for _ in range(10 ** 5)]
print(energy)
k = 1000

solution = Solution()
print(solution.maximumEnergy(energy, k))
