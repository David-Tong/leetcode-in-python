class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        from collections import deque
        bfs = deque()

        M = len(matrix)
        N = len(matrix[0])
        vistied = [[1] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                bfs.append((x, y))

        ans = 1
        while bfs:
            x, y = bfs.popleft()
            for direction in DIRECTIONS:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if new_x >= 0 and new_x < M and \
                    new_y >= 0 and new_y < N:
                    if matrix[new_x][new_y] > matrix[x][y]:
                        if vistied[new_x][new_y] < vistied[x][y] + 1:
                            vistied[new_x][new_y] = vistied[x][y] + 1
                            bfs.append((new_x, new_y))
                            ans = max(ans, vistied[new_x][new_y])

        return ans


matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [[1]]

solution = Solution()
print(solution.longestIncreasingPath(matrix))
