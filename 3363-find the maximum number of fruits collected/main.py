class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(fruits)
        DIRECTIONS = (((-1, -1), (-1, 0), (-1, 1)), ((-1, -1), (0, -1), (1, -1)))

        # process
        # child one can collect fruits in the diagonal only
        ones = 0
        for x in range(M):
            ones += fruits[x][x]
            fruits[x][x] = 0

        # child two can collect fruits in the upper triangular matrix only
        # twos[x][y] - the maximum number of all fruits the child two can collect at fruits[x][y]
        twos = [[0] * M for _ in range(M)]
        visited = [[False] * M for _ in range(M)]
        twos[0][M - 1] = fruits[0][M - 1]
        visited[0][M - 1] = True

        for x in range(1, M):
            for y in range(x, M):
                maxi = 0
                pvisit = False
                for dx, dy in DIRECTIONS[0]:
                    px, py = x + dx, y + dy
                    if 0 <= px < M and 0 <= py < M and visited[px][py]:
                        maxi = max(maxi, twos[px][py])
                        pvisit = True
                if pvisit:
                    twos[x][y] = fruits[x][y] + maxi
                    visited[x][y] = True

        # print(twos)

        # child three can collect fruits in the lower triangular matrix only
        # threes[x][y] - the maximum number of all fruits the child three can collect at fruits[x][y]
        threes = [[0] * M for _ in range(M)]
        visited = [[False] * M for _ in range(M)]
        threes[M - 1][0] = fruits[M - 1][0]
        visited[M - 1][0] = True

        for y in range(1, M):
            for x in range(y, M):
                maxi = 0
                pvisit = False
                for dx, dy in DIRECTIONS[1]:
                    px, py = x + dx, y + dy
                    if 0 <= px < M and 0 <= py < M and visited[px][py]:
                        maxi = max(maxi, threes[px][py])
                        pvisit = True
                if pvisit:
                    threes[x][y] = fruits[x][y] + maxi
                    visited[x][y] = True

        # print(threes)

        ans = ones + twos[M - 1][M - 1] + threes[M - 1][M - 1]
        return ans


fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
fruits = [[1,1],[1,1]]
fruits = [[16,3,11,14,14],[3,0,10,13,14],[7,18,8,7,18],[7,8,5,7,5],[0,14,8,1,0]]

from random import randint
fruits = [[randint(0, 1000) for _ in range(250)] for _ in range(250)]
print(fruits)

solution = Solution()
print(solution.maxCollectedFruits(fruits))
