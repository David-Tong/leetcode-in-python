class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degrees = [0] * n
        from collections import defaultdict
        adjacents = defaultdict(list)
        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1
            adjacents[road[0]].append(road[1])
            adjacents[road[1]].append(road[0])

        ans = 0
        for x in range(n):
            for y in range(x + 1, n):
                if y not in adjacents[x]:
                    ans = max(ans, degrees[x] + degrees[y])
                else:
                    ans = max(ans, degrees[x] + degrees[y] - 1)
        return ans


n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]

n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

n = 2
roads = []

solution = Solution()
print(solution.maximalNetworkRank(n, roads))
