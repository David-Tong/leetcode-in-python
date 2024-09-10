class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        N = len(roads) + 1

        from collections import defaultdict
        tree = defaultdict(list)
        visited = [False] * N
        visited[0] = True

        for road in roads:
            tree[road[0]].append(road[1])
            tree[road[1]].append(road[0])

        def doCost(node):
            cost = 0
            nodes = 1
            for child in tree[node]:
                if not visited[child]:
                    visited[child] = True
                    child_cost, child_nodes = doCost(child)
                    cost += child_cost
                    nodes += child_nodes

            if node != 0:
                if nodes % seats == 0:
                    cost += nodes // seats
                else:
                    cost += nodes // seats + 1
            return cost, nodes

        ans, _ = doCost(0)
        return ans


roads = [[0,1],[0,2],[0,3]]
seats = 5

roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2

roads = []
seats = 1

solution = Solution()
print(solution.minimumFuelCost(roads, seats))
