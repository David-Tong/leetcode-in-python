class Solution(object):
    def maxBalancedShipments(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        # pre-process
        L = len(weight)

        # process
        maxi = 0
        ans = 0
        for x in range(L):
            maxi = max(maxi, weight[x])
            if weight[x] < maxi:
                ans += 1
                maxi = 0
        return ans


weight = [2,5,1,4,3]
weight = [4,4]

from random import randint
weight = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(weight)

solution = Solution()
print(solution.maxBalancedShipments(weight))
