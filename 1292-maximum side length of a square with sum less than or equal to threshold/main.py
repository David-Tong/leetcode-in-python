class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        M = len(mat)
        N = len(mat[0])

        # presum
        presum = [[0] * (N + 1) for _ in range(M + 1)]
        for x in range(M):
            for y in range(1, N + 1):
                presum[x + 1][y] = presum[x + 1][y - 1] + mat[x][y - 1]

        for x in range(1, M + 1):
            for y in range(1, N + 1):
                presum[x][y] += presum[x - 1][y]

        def getSquareSum(x, y, target):
            nx = x + target - 1
            ny = y + target - 1
            return presum[nx + 1][ny + 1] - presum[x][ny + 1] - presum[nx + 1][y] + presum[x][y]

        def doHave(target):
            for x in range(M):
                for y in range(N):
                    if x + target > M or y + target > N:
                        pass
                    else:
                        square = getSquareSum(x, y, target)
                        if square <= threshold:
                            return True
            return False

        left = 1
        right = min(M, N)

        while left + 1 < right:
            middle = (left + right) // 2
            if doHave(middle):
                left = middle
            else:
                right = middle - 1

        if doHave(right):
            return right
        elif doHave(left):
            return left
        else:
            return 0


mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4

mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
threshold = 1

mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
threshold = 40184

solution = Solution()
print(solution.maxSideLength(mat, threshold))
