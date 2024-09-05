class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(rowSum)
        N = len(colSum)

        # process
        ans = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                val = min(rowSum[x], colSum[y])
                ans[x][y] = val
                rowSum[x] -= val
                colSum[y] -= val
        return ans


rowSum = [3,8]
colSum = [4,7]

rowSum = [5,7,10]
colSum = [8,6,8]

solution = Solution()
print(solution.restoreMatrix(rowSum, colSum))