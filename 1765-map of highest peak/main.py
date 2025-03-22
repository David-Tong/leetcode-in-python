from multiprocessing.managers import view_types


class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(isWater)
        N = len(isWater[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # process
        # bfs
        ans = [[-1] * N for _ in range(M)]
        from collections import deque
        bfs = deque()
        for x in range(M):
            for y in range(N):
                if isWater[x][y] == 1:
                    bfs.append((0, x, y))
                    ans[x][y] = 0

        while bfs:
            height, x, y = bfs.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if ans[nx][ny] == -1:
                        ans[nx][ny] = height + 1
                        bfs.append((height + 1, nx, ny))
        return ans


isWater = [[0,1],[0,0]]
isWater = [[0,0,1],[1,0,0],[0,0,0]]

solution = Solution()
print(solution.highestPeak(isWater))
