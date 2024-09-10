class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        # dp init
        # dp - contains all possible the sum of chosen elements
        M = len(mat)
        N = len(mat[0])
        dp = set()
        dp.add(0)

        # dp transfer
        for x in range(M):
            ndp = set()
            for d in dp:
                for y in range(N):
                    ndp.add(d + mat[x][y])
            dp = ndp

        # dp answer
        ans = float("inf")
        for d in dp:
            ans = min(ans, abs(target - d))
        return ans


mat = [[1,2,3],[4,5,6],[7,8,9]]
target = 13

mat = [[1],[2],[3]]
target = 100

mat = [[1,2,9,8,7]]
target = 6

mat = [[1] * 70 for _ in range(70)]
target = 80

solution = Solution()
print(solution.minimizeTheDifference(mat, target))
