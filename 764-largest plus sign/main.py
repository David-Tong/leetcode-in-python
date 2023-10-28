class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        def canPlus(k):
            for x in range(k - 1, n - k + 1):
                for y in range(k - 1, n - k + 1):
                    if prerows[x][y + k] - prerows[x][y - k + 1] == 2 * k - 1 and precols[y][x + k] - precols[y][x - k + 1] == 2 * k - 1:
                        return True
            return False

        grid = [[True] * n for _ in range(n)]
        for mine in mines:
            grid[mine[0]][mine[1]] = False

        # presum for rows
        prerows = list()
        for x in range(n):
            prerow = list()
            presum = 0
            prerow.append(presum)
            for y in range(n):
                if grid[x][y]:
                    presum += 1
                prerow.append(presum)
            prerows.append(prerow)

        # presum for cols
        precols = list()
        for y in range(n):
            precol = list()
            presum = 0
            precol.append(presum)
            for x in range(n):
                if grid[x][y]:
                    presum += 1
                precol.append(presum)
            precols.append(precol)

        # binary search
        left = 0
        if n % 2 == 0:
            right = n // 2
        else:
            right = n // 2 + 1

        while left + 1 < right:
            middle = (left + right) // 2
            if canPlus(middle):
                left = middle
            else:
                right = middle - 1

        if canPlus(right):
            return right
        else:
            return left


n = 5
mines = [[4,2]]

n = 1
mines = [[0,0]]

n = 2
mines = [[0,0], [1,1]]

solution = Solution()
print(solution.orderOfLargestPlusSign(n, mines))
