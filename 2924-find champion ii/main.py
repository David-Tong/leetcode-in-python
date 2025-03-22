class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        out_degrees = [0] * n
        for edge in edges:
            out_degrees[edge[1]] += 1

        # process
        ans = 0
        champions = 0
        for idx, out_degree in enumerate(out_degrees):
            if out_degree == 0:
                champions += 1
                ans = idx

        return ans if champions == 1 else -1


n = 3
edges = [[0,1],[1,2]]

n = 4
edges = [[0,2],[1,3],[1,2]]

solution = Solution()
print(solution.findChampion(n, edges))
