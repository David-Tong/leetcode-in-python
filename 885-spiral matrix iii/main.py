class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        # pre-process
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ans = list()
        step = 1
        direction = 0
        r, c = rStart, cStart

        # process
        while len(ans) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                    r = r + DIRECTIONS[direction][0]
                    c = c + DIRECTIONS[direction][1]
                direction = (direction + 1) % 4
            step += 1
        return ans


rows = 1
cols = 4
rStart = 0
cStart = 0

rows = 5
cols = 6
rStart = 1
cStart = 4

solution = Solution()
print(solution.spiralMatrixIII(rows, cols, rStart, cStart))
