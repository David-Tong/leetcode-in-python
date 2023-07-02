class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def canCross(day):
            matrix = [[0] * col for _ in range(row)]
            for cell in cells[:day]:
                x, y = cell[0] - 1, cell[1] - 1
                matrix[x][y] = 1

            from collections import deque
            bfs = deque()
            visited = [[False] * col for _ in range(row)]
            for y in range(col):
                if matrix[0][y] == 0:
                    bfs.append((0, y))
                    visited[0][y] = True

            while bfs:
                x, y = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col:
                        if matrix[nx][ny] == 0:
                            if nx == row - 1:
                                return True
                            if not visited[nx][ny]:
                                bfs.append((nx, ny))
                                visited[nx][ny] = True
            return False

        left = 1
        right = len(cells)

        while left + 1 < right:
            middle = (left + right) // 2
            if canCross(middle):
                left = middle
            else:
                right = middle - 1

        if canCross(right):
            return right
        else:
            return left


row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]

row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]

row = 3
col = 3
cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

solution = Solution()
print(solution.latestDayToCross(row, col, cells))
