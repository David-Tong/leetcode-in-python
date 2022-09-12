class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        MOD = 10 ** 9 + 7

        prev = [[0] * n for _ in range(m)]
        curr = [[0] * n for _ in range(m)]
        prev[startRow][startColumn] = 1

        move = 0
        ans = 0
        while move < maxMove:
            for x in range(m):
                for y in range(n):
                    for delta_x, delta_y in DIRECTIONS:
                        new_x = x + delta_x
                        new_y = y + delta_y
                        if 0 <= new_x < m and 0 <= new_y < n:
                            curr[new_x][new_y] += prev[x][y]
                        else:
                            ans += prev[x][y]
                            ans %= MOD
            prev = curr
            curr = [[0] * n for _ in range(m)]
            move += 1

        return ans


m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1

m = 8
n = 50
maxMove = 23
startRow = 5
startColumn = 26

solution = Solution()
print(solution.findPaths(m, n, maxMove, startRow, startColumn))
