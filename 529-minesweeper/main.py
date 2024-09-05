class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        M = len(board)
        N = len(board[0])

        def reveal(x, y):
            if board[x][y] == "M":
                return "X"
            elif board[x][y] == "E":
                count = 0
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if board[nx][ny] == "M":
                            count += 1
                if count == 0:
                    return "B"
                else:
                    return str(count)
            else:
                return board[x][y]

        def isRevealed(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if board[nx][ny] == 'M' or ans[nx][ny] == 'X':
                        return True
            return False

        from copy import deepcopy
        ans = deepcopy(board)
        x, y = click[0], click[1]
        ans[x][y] = reveal(x, y)

        from collections import deque
        bfs = deque()
        visited = [[False] * N for _ in range(M)]

        if board[x][y] == "E" and not isRevealed(x, y):
            bfs.append((x, y))
            visited[x][y] = True

        while bfs:
            x, y = bfs.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[nx][ny]:
                        ans[nx][ny] = reveal(nx, ny)
                        visited[nx][ny] = True
                        if ans[nx][ny] == "B" and not isRevealed(nx, ny):
                            bfs.append((nx, ny))
        return ans


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]

board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]

board = [["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]
click = [0,7]

board = [["E","M","M","2","B","B","B","B"],["E","E","M","2","B","B","B","B"],["E","E","2","1","B","B","B","B"],["E","M","1","B","B","B","B","B"],["1","2","2","1","B","B","B","B"],["B","1","M","1","B","B","B","B"],["B","1","1","1","B","B","B","B"],["B","B","B","B","B","B","B","B"]]
click = [0,0]

solution = Solution()
print(solution.updateBoard(board, click))
