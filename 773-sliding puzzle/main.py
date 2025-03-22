from copy import deepcopy


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # pre-process
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        M = len(board)
        N = len(board[0])

        def getKey(board):
            key = ""
            for x in range(M):
                for y in range(N):
                    key += "-" + str(board[x][y])
            return key

        # shortcut
        TARGET_BOARD = [[1, 2, 3], [4, 5, 0]]
        TARGET_KEY = getKey(TARGET_BOARD)
        if getKey(board) == TARGET_KEY:
            return 0

        for x in range(M):
            for y in range(N):
                if board[x][y] == 0:
                    zero = (x, y)
                    break

        from collections import deque
        bfs = deque()
        from copy import deepcopy
        board = deepcopy(board)
        bfs.append((board, zero))
        from collections import defaultdict
        visited = defaultdict(bool)
        key = getKey(board)
        visited[key] = True

        # process
        step = 0
        while bfs:
            step += 1
            L = len(bfs)
            for _ in range(L):
                board, zero = bfs.popleft()
                # print(board, zero)
                x, y = zero
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        nboard = deepcopy(board)
                        nboard[x][y] = nboard[nx][ny]
                        nboard[nx][ny] = 0
                        nkey = getKey(nboard)
                        nzero = (nx, ny)
                        if nkey == TARGET_KEY:
                            return step
                        if nkey not in visited:
                            visited[nkey] = True
                            bfs.append((nboard, nzero))
        return -1


board = [[1,2,3],[4,0,5]]
board = [[1,2,3],[5,4,0]]
board = [[4,1,2],[5,0,3]]
board = [[2,1,4],[3,0,5]]
board = [[2,1,4],[3,5,0]]

solution = Solution()
print(solution.slidingPuzzle(board))
