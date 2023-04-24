class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        matrix = [[1] * n for _ in range(m)]
        for guard in guards:
            matrix[guard[0]][guard[1]] = 'G'
        for wall in walls:
            matrix[wall[0]][wall[1]] = 'W'

        def countGuarded(guard):
            gx = guard[0]
            gy = guard[1]
            # count row, left first then right
            y = gy - 1
            while y >= 0:
                if matrix[gx][y] in ('G', 'W'):
                    break
                else:
                    matrix[gx][y] = 0
                y -= 1

            y = gy + 1
            while y < n:
                if matrix[gx][y] in ('G', 'W'):
                    break
                else:
                    matrix[gx][y] = 0
                y += 1

            # count column, top first then down
            x = gx - 1
            while x >= 0:
                if matrix[x][gy] in ('G', 'W'):
                    break
                else:
                    matrix[x][gy] = 0
                x -= 1

            x = gx + 1
            while x < m:
                if matrix[x][gy] in ('G', 'W'):
                    break
                else:
                    matrix[x][gy] = 0
                x += 1

        for guard in guards:
            countGuarded(guard)

        for guard in guards:
            matrix[guard[0]][guard[1]] = 0
        for wall in walls:
            matrix[wall[0]][wall[1]] = 0

        ans = 0
        for row in matrix:
            ans += sum(row)
        return ans


m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]

m = 3
n = 3
guards = [[1,1]]
walls = [[0,1],[1,0],[2,1],[1,2]]

solution = Solution()
print(solution.countUnguarded(m, n, guards, walls))
