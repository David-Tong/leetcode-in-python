class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        vertices = set()
        vertices.add(edges[0][0])
        vertices.add(edges[0][1])

        # process
        if edges[1][0] in vertices:
            return edges[1][0]
        else:
            return edges[1][1]


edges = [[1,2],[2,3],[4,2]]
edges = [[1,2],[5,1],[1,3],[1,4]]

solution = Solution()
print(solution.findCenter(edges))
