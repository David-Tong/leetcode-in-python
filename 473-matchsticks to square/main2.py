class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        L = len(matchsticks)
        visited = [0] * L
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        limit = total // 4

        def dfs(idx, group, edge):
            if group == 4:
                return True
            if edge > limit:
                return False
            if edge == limit:
                return dfs(0, group + 1, 0)

            for x in range(idx, L):
                if visited[x] == 1:
                    continue
                visited[x] = 1
                if dfs(x + 1, group, edge + matchsticks[x]):
                    return True
                visited[x] = 0
            return False

        return dfs(0, 0, 0)


matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
matchsticks = [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
matchsticks = [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]

solution = Solution()
print(solution.makesquare(matchsticks))
