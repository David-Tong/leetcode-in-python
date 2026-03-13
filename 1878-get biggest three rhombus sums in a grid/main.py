import heapq


class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        M, N = len(grid), len(grid[0])
        diagonal = [[0 for _ in range(N)] for _ in range(M)]
        for x in range(M):
            for y in range(N):
                diagonal[x][y] = grid[x][y]
                if x > 0 and y > 0:
                    diagonal[x][y] += diagonal[x - 1][y - 1]
        # print(diagonal)

        antidiagonal = [[0 for _ in range(N)] for _ in range(M)]
        for x in range(M):
            for y in range(N):
                antidiagonal[x][y] = grid[x][y]
                if x > 0 and y < N - 1:
                    antidiagonal[x][y] += antidiagonal[x - 1][y + 1]
        # print(antidiagonal)

        # helper function
        def side(sx, sy, ex, ey, d):
            if d == 1:
                if sx == 0 or sy == 0:
                    return diagonal[ex][ey]
                else:
                    return diagonal[ex][ey] - diagonal[sx - 1][sy - 1]
            elif d == -1:
                if sx == 0 or sy == N - 1:
                    return antidiagonal[ex][ey]
                else:
                    return antidiagonal[ex][ey] - antidiagonal[sx - 1][sy + 1]
            else:
                raise ValueError("d must be 1 or -1")

        def perimeter(p1, p2, p3, p4):
            total = 0
            total += side(p1[0], p1[1], p2[0], p2[1], 1)
            total += side(p2[0], p2[1], p3[0], p3[1], -1)
            total += side(p4[0], p4[1], p3[0], p3[1], 1)
            total += side(p1[0], p1[1], p4[0], p4[1], -1)
            total -= grid[p1[0]][p1[1]] + grid[p2[0]][p2[1]] + grid[p3[0]][p3[1]] + grid[p4[0]][p4[1]]
            return total

        # print(perimeter((1, 1), (2, 2), (3, 1), (0, 2)))

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        s = set()

        for x in range(M):
            for y in range(N):
                total = grid[x][y]
                if total not in s:
                    heappush(heap, total)
                    if len(heap) > 3:
                        heappop(heap)
                    s.add(total)

        for x in range(M):
            for y in range(N):
                # decide a rhombus
                for k in range(1, min(M, N) + 1):
                    p1 = x, y
                    if x + k < M and y + k < N:
                        p2 = x + k, y + k
                    else:
                        break
                    if x + 2 * k < M:
                        p3 = x + 2 * k, y
                    else:
                        break
                    if x + k < M and y - k >= 0:
                        p4 = x + k, y - k
                    else:
                        break
                    total = perimeter(p1, p2, p3, p4)
                    if total not in s:
                        heappush(heap, total)
                        if len(heap) > 3:
                            heappop(heap)
                        s.add(total)

        ans = list()
        while heap:
            ans.append(heappop(heap))
        ans = ans[::-1]
        return ans


grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[7,7,7]]

from random import randint
grid = [[randint(1, 10 ** 5) for _ in range(50)] for _ in range(50)]
print(grid)

solution = Solution()
print(solution.getBiggestThree(grid))
