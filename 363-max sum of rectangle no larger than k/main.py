class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        M = len(matrix)
        N = len(matrix[0])

        # calculate column prefixes
        columns = [[0] * N for _ in range(M + 1)]
        for x in range(1, M + 1):
            for y in range(N):
                columns[x][y] = columns[x - 1][y] + matrix[x - 1][y]

        # calculate sum of rectangles
        from bisect import bisect_left
        diff = float("inf")
        ans = float("inf")
        for x in range(M + 1):
            for y in range(x + 1, M + 1):
                curr = list()
                for z in range(N):
                    curr.append(columns[y][z] - columns[x][z])

                # calculate row prefixes
                rows = [0] * (N + 1)
                targets = [0]
                for z in range(1, N + 1):
                    rows[z] = rows[z - 1] + curr[z - 1]

                    # search for target
                    target = rows[z] - k
                    idx = bisect_left(targets, target)
                    if idx < z:
                        rectangle = rows[z] - targets[idx]
                        if k - rectangle < diff:
                            diff = k - rectangle
                            ans = rectangle
                            if diff == 0:
                                return ans

                    # insert to targets
                    idx = bisect_left(targets, rows[z])
                    targets = targets[:idx] + [rows[z]] + targets[idx:]

        return ans


matrix = [[1,0,1],[0,-2,3]]
k = 2

matrix = [[2,2,-1]]
k = 3

solution = Solution()
print(solution.maxSumSubmatrix(matrix, k))
