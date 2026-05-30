class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        C = 3
        N = len(grid)
        M = N // 2
        ys = [0] * 3
        os = [0] * 3

        for x in range(N):
            for y in range(N):
                idx = grid[x][y]
                os[idx] += 1

        # draw Y
        idx = 0
        while idx < M:
            c = grid[idx][idx]
            ys[c] += 1
            idx += 1


        idx = 0
        while idx < M:
            c = grid[idx][N - idx - 1]
            ys[c] += 1
            idx += 1

        idx = M
        while idx < N:
            c = grid[idx][M]
            ys[c] += 1
            idx += 1

        for c in range(C):
            os[c] -= ys[c]

        # print(ys)
        # print(os)

        # process
        # helper function
        def calculate(c0, c1):
            # set y to c0, others to c1
            res = 0
            for c in range(C):
                if c != c0:
                   res += ys[c]
                if c != c1:
                    res += os[c]
            return res

        ans = float("inf")
        for c in range(C):
            for c2 in range(C):
                if c != c2:
                    ans = min(ans, calculate(c, c2))
        return ans


grid = [[1,2,2],[1,1,0],[0,1,0]]
grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]

import random
grid = [[random.choice([0, 1, 2]) for _ in range(49)] for _ in range(49)]
print(grid)

solution = Solution()
print(solution.minimumOperationsToWriteY(grid))
