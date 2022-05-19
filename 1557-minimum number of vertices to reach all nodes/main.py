class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_degrees = [0] * n
        out_degrees = [0] * n
        for edge in edges:
            out_degrees[edge[0]] += 1
            in_degrees[edge[1]] += 1

        ans = []
        for idx, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                ans.append(idx)
        return ans


n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]

solution = Solution()
print(solution.findSmallestSetOfVertices(n, edges))
