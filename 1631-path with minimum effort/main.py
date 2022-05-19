class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        M = len(heights)
        N = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        if M == 1 and N == 1:
            return 0

        def doPath(heights, height):
            from collections import deque
            bfs = deque()
            bfs.append((0, 0))
            visited = [[0] * N for _ in range(M)]
            visited[0][0] = 1
            while bfs:
                x, y = bfs.popleft()
                for direction in DIRECTIONS:
                    nx = x + direction[0]
                    ny = y + direction[1]
                    if 0 <= nx < M and 0 <= ny < N:
                        if abs(heights[nx][ny] - heights[x][y]) <= height:
                            if nx == M - 1 and ny == N - 1:
                                return True
                            else:
                                if visited[nx][ny] == 0:
                                    bfs.append((nx, ny))
                                    visited[nx][ny] = 1
            return False

        left = 0
        right = 10 ** 6

        while left + 1 < right:
            middle = (left + right) // 2
            if doPath(heights, middle):
                right = middle
            else:
                left = middle

        if doPath(heights, left):
            return left
        elif doPath(heights, right):
            return right


heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1,10,6,7,9,10,4,9]]
heights = [[1, 10 ** 6], [1, 10 ** 6]]
heights = [[3]]
#heights = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]

solution = Solution()
print(solution.minimumEffortPath(heights))