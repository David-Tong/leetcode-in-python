class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # bfs
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        from collections import deque
        bfs = deque()
        bfs.append(start)

        visited = [[False] * N for _ in range(M)]
        visited[start[0]][start[1]] = True

        distance = 0

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1]:
            heappush(heap, (distance, grid[start[0]][start[1]], start[0], start[1]))

        while bfs and len(heap) < k:
            size = len(bfs)
            distance += 1
            for _ in range(size):
                x, y = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if grid[nx][ny] != 0:
                            if not visited[nx][ny]:
                                bfs.append((nx, ny))
                                visited[nx][ny] = True
                                if pricing[0] <= grid[nx][ny] <= pricing[1]:
                                    heappush(heap, (distance, grid[nx][ny], nx, ny))

        count = 0
        ans = list()
        while heap and count < k:
            _, _, x, y = heappop(heap)
            count += 1
            ans.append([x, y])
        return ans


grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
pricing = [2,5]
start = [0,0]
k = 3

grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]]
pricing = [2,3]
start = [2,3]
k = 2

grid = [[1,1,1],[0,0,1],[2,3,4]]
pricing = [2,3]
start = [0,0]
k = 3

grid = [[1]]
pricing = [2,5]
start = [0,0]
k = 1

"""
grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]]
pricing = [2,3]
start = [1,1]
k = 1

grid = [[57,54,48],[652,572,990],[632,199,306],[38,702,263],[431,0,507],[673,570,750],[316,141,639]]
pricing = [475,745]
start = [3,2]
k = 4
"""

solution = Solution()
print(solution.highestRankedKItems(grid, pricing, start, k))
