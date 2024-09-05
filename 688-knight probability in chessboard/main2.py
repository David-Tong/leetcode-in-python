class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        DIRECTIONS = ((-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2))
        from collections import deque
        bfs = deque()
        bfs.append((row, column, 1))

        for i in range(k):
            size = len(bfs)
            for j in range(size):
                x, y, p = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        bfs.append((nx, ny, p / 8.0))

        ans = 0
        for x, y, p in bfs:
            ans += p
        return ans


n = 3
k = 2
row = 0
column = 0

n = 1
k = 0
row = 0
column = 0

n = 25
k = 100
row = 5
column = 20

solution = Solution()
print(solution.knightProbability(n, k, row, column))
