class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if sum(matchsticks) % 4 != 0:
            return False

        edges = [0] * 4
        limit = sum(matchsticks) // 4

        matchsticks = sorted(matchsticks, reverse=True)

        def dfs(idx):
            if idx == len(matchsticks):
                return True
            else:
                for x in range(4):
                    edges[x] += matchsticks[idx]
                    if edges[x] <= limit and dfs(idx + 1):
                        return True
                    edges[x] -= matchsticks[idx]
                return False

        return dfs(0)


matchsticks = [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
matchsticks = [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]

solution = Solution()
print(solution.makesquare(matchsticks))
