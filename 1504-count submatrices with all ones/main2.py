class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])
        cols = [[0] * N for _ in range(M + 1)]
        for x in range(M):
            for y in range(N):
                cols[x + 1][y] = cols[x][y] + mat[x][y]
        # print(cols)


        # process
        # o(n ** 3) solution, find valid sub matrices between two rows
        ans = 0
        for x in range(M):
            for ox in range(x, M):
                h = ox + 1 - x
                # go to find the number of rectangles with h and use ox as bottom
                hs = list()
                for y in range(N):
                    if cols[ox + 1][y] - cols[x][y] == h:
                        if hs and hs[-1] > 0:
                            hs[-1] += 1
                        else:
                            hs.append(1)
                    else:
                        hs.append(0)
                # count continuous histograms
                # print(x, ox + 1, h)
                # print(hs)
                for s in hs:
                    if s > 0:
                        ans += s * (s + 1) // 2
        return ans


mat = [[1,0,1],[1,1,0],[1,1,0]]
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]

solution = Solution()
print(solution.numSubmat(mat))