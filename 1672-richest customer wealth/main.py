class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        M = len(accounts)
        wealths = [0] * M
        for x in range(M):
            wealths[x] = sum(accounts[x])
        return max(wealths)


accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]
accounts = [[2,8,7],[7,1,3],[1,9,5]]

solution = Solution()
print(solution.maximumWealth(accounts))
