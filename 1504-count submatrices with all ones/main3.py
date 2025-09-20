class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])

        # dp init
        presum = [[0] * (N + 1) for _ in range(M + 1)]
        presum[1][1] = mat[0][0]
        for x in range(1, M):
            presum[x + 1][1] = presum[x][1] + mat[x][0]
        for y in range(1, N):
            presum[1][y + 1] = presum[1][y] + mat[0][y]

        # dp transfer
        for x in range(1, M):
            for y in range(1, N):
                presum[x + 1][y + 1] = presum[x + 1][y] + presum[x][y + 1] - presum[x][y] + mat[x][y]
        print(presum)

        # process
        # o(n ** 4) solution, enumerate all sub matrices and validate
        ans = 0
        for x in range(M + 1):
            for y in range(N + 1):
                for ox in range(x + 1, M + 1):
                    for oy in range(y + 1, N + 1):
                        expected = (ox - x) * (oy - y)
                        area = presum[ox][oy] - presum[x][oy] - presum[ox][y] + presum[x][y]
                        if expected == area:
                            ans += 1
                        if expected < area:
                            break
        return ans


mat = [[1,0,1], [1,1,0], [1,1,0]]
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]

solution = Solution()
print(solution.numSubmat(mat))