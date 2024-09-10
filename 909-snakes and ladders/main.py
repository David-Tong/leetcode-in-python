class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        # label the board
        label = 1
        labels = list()
        labels.append(())
        matrix = [[0] * N for _ in range(N)]

        while label <= N * N:
            x = N - 1 - (label - 1) // N
            if (N - 1 - x) % 2 == 0:
                y = (label - 1) % N
            else:
                y = N - 1 - (label - 1) % N

            matrix[x][y] = label
            labels.append((x, y))
            label += 1

        from collections import deque
        bfs = deque()
        visited = [False] * (N * N + 1)

        bfs.append(1)
        visited[1] = True

        ans = 1
        while bfs:
            L = len(bfs)
            for x in range(L):
                curr = bfs.popleft()
                for nxt in range(curr + 1, min(curr + 6, N * N) + 1):
                    nx, ny = labels[nxt][0], labels[nxt][1]
                    if nxt == N * N or board[nx][ny] == N * N:
                        return ans
                    if not visited[nxt]:
                        visited[nxt] = True
                        if board[nx][ny] == -1:
                            bfs.append(nxt)
                        else:
                            bfs.append(board[nx][ny])
            ans += 1
        return -1


board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,14,-1,-1,-1,-1]]
board = [[-1,-1],[-1,3]]
board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]

solution = Solution()
print(solution.snakesAndLadders(board))
