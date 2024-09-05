class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # pre-process
        degrees = [0] * n
        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1
        print(degrees)

        # process
        degrees = sorted(degrees)
        ans = 0
        for x in range(n):
            ans += (x + 1) * degrees[x]
        return ans


n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

n = 5
roads = [[0,3],[2,4],[1,3]]

solution = Solution()
print(solution.maximumImportance(n, roads))
