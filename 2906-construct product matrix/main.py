class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        MODULO = 12345
        M = len(grid)
        N = len(grid[0])

        arr = []
        for x in range(M):
            for y in range(N):
                arr.append(grid[x][y])

        prefix = [1]
        for x in arr:
            prefix.append((prefix[-1] * x) % MODULO)
        print(prefix)

        suffix = [1]
        for x in arr[::-1]:
            suffix.append((suffix[-1] * x) % MODULO)
        suffix = suffix[::-1]
        print(suffix)

        # calculate
        from collections import deque
        q = deque()
        for x in range(len(arr)):
            q.append((prefix[x] * suffix[x + 1]) % MODULO)

        ans = [[None] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                ans[x][y] = q.popleft()
        return ans


grid = [[1,2],[3,4]]
grid = [[12345],[2],[1]]
grid = [[3,2,5],[6,4,3],[6,3,1]]

solution = Solution()
print(solution.constructProductMatrix(grid))
