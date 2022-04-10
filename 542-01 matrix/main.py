class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        def isValid(mat, x, y):
            if x < 0 or x >= len(mat) or \
                y < 0 or y >= len(mat[0]):
                return False
            else:
                return True

        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        MAX_DIST = len(mat) + len(mat[0])

        from collections import deque
        bfs = deque()
        ans = []

        for i in range(len(mat)):
            row = [0] * len(mat[0])
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    bfs.append((i, j))
                else:
                    row[j] = MAX_DIST
            ans.append(row)

        while len(bfs) > 0:
            x, y = bfs.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x, next_y = x + delta_x, y + delta_y
                if isValid(mat, next_x, next_y) and \
                    ans[next_x][next_y] > ans[x][y] + 1:
                    ans[next_x][next_y] = ans[x][y] + 1
                    bfs.append((next_x, next_y))

        return ans


mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]

solution = Solution()
print(solution.updateMatrix(mat))
