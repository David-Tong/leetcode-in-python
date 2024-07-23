class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        L = len(cost)
        cost = sorted(cost, reverse=True)

        ans = sum(cost)
        for x in range(2, L, 3):
            ans -= cost[x]
        return ans


cost = [1,2,3]
cost = [6,5,7,9,2,2]
cost = [5,5]

solution = Solution()
print(solution.minimumCost(cost))
