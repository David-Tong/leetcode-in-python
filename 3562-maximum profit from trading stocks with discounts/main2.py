class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        # pre-process
        graph = [[] for _ in range(n)]
        for x, y in hierarchy:
            graph[x - 1].append(y - 1)

        # process
        def dfs(parent):
            # calculate subtree
            # dp[x, 0] - the maximum profit for a subtree with budget x when parent is not purchased
            # dp[x, 1] - the maximum profit for a subtree with budget x when parent is purchase
            dp_sub = [[0, 0] for _ in range(budget + 1)]
            for child in graph[parent]:
                dp_child = dfs(child)
                for b in range(budget, -1, -1):
                    for b_child in range(b + 1):
                        for k in range(2):
                            dp_sub[b][k] = max(dp_sub[b][k], dp_sub[b - b_child][k] + dp_child[b_child][k])

            # calculate parent
            dp = [[0, 0] for _ in range(budget + 1)]
            for b in range(budget + 1):
                for k in range(2):
                    cost = present[parent] // (k + 1)
                    if b >= cost:
                        # buy or not buy
                        dp[b][k] = max(dp_sub[b][0], dp_sub[b - cost][1] + future[parent] - cost)
                    else:
                        dp[b][k] = dp_sub[b][0]
            return dp

        return dfs(0)[budget][0]


n = 2
present = [1,2]
future = [4,3]
hierarchy = [[1,2]]
budget = 3

n = 2
present = [3, 4]
future = [5, 8]
hierarchy = [[1, 2]]
budget = 4

n = 3
present = [4,6,8]
future = [7,9,11]
hierarchy = [[1,2],[1,3]]
budget = 10

n = 3
present = [5,2,3]
future = [8,5,6]
hierarchy = [[1,2],[2,3]]
budget = 7

n = 2
present = [6, 11]
future = [5, 48]
hierarchy = [[1,2]]
budget = 142

n = 3
present = [26,17,11]
future = [40,46,13]
hierarchy = [[1,3],[3,2]]
budget = 98

n = 3
present = [6,4,23]
future = [50,48,17]
hierarchy = [[1,3],[1,2]]
budget = 28

solution = Solution()
print(solution.maxProfit(n, present, future, hierarchy, budget))
