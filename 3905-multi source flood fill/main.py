class Solution(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        sources = sorted(sources, key=lambda x: (x[2], x[0], x[1]), reverse=True)

        # process
        from collections import deque
        bfs = deque()
        visited = [[False] * m for _ in range(n)]
        ans = [[0] * m for _ in range(n)]

        for source in sources:
            bfs.append(source)
            visited[source[0]][source[1]] = True
            ans[source[0]][source[1]] = source[2]

        # bfs
        while bfs:
            size = len(bfs)
            for _ in range(size):
                x, y, color = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if not visited[nx][ny]:
                            bfs.append([nx, ny, color])
                            visited[nx][ny] = True
                            ans[nx][ny] = color
        return ans


n = 3
m = 3
sources = [[0,0,1],[2,2,2]]

n = 3
m = 3
sources = [[0,1,3],[1,1,5]]

n = 2
m = 2
sources = [[1,1,5]]

solution = Solution()
print(solution.colorGrid(n, m, sources))
