class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        # pre-process
        numbers = list()
        for row in range(N):
            zeros = 0
            for col in range(N - 1, -1, -1):
                if grid[row][col] != 0:
                    numbers.append(zeros)
                    break
                zeros += 1
            if zeros == N:
                numbers.append(zeros)

        ans = 0
        for row in range(N):
            if numbers[row] < N - 1 - row:
                found = False
                for row2 in range(row, N):
                    if numbers[row2] >= N - 1 - row:
                        # swap
                        numbers = numbers[:row] + [numbers[row2]] + numbers[row:row2] + numbers[row2 + 1:]
                        ans += row2 - row
                        found = True
                        break
                if not found:
                    return -1
        return ans


grid = [[0,0,1],[1,1,0],[1,0,0]]
grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
grid = [[1,0,0],[1,1,0],[1,1,1]]
grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
grid = [[0,0],[0,1]]

solution = Solution()
print(solution.minSwaps(grid))
