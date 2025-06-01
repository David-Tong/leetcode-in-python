class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(moveTime)
        N = len(moveTime[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # process
        # dijkstra's algorithm
        distances = [[-1] * N for _ in range(M)]
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        heappush(heap, (0, 0, 0, 0))
        while heap:
            t, x, y, step = heappop(heap)
            if distances[x][y] == -1:
                step += 1
                distances[x][y] = t
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        dt = 1 if step % 2 == 1 else 2
                        nt = max(moveTime[nx][ny], t) + dt
                        if nx == M - 1 and ny == N - 1:
                            return nt
                        if distances[nx][ny] == -1:
                            heappush(heap, (nt, nx, ny, step))


moveTime = [[0,4],[4,4]]
moveTime = [[0,0,0,0],[0,0,0,0]]
moveTime = [[0,1],[1,2]]
moveTime = [[4,13,67],[20,24,57]]

solution = Solution()
print(solution.minTimeToReach(moveTime))
