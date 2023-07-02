class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        M = len(mat)
        N = len(mat[0])
        
        odds = list()
        for x in range(M):
            odds.append((x, 0))
        for y in range(1, N):
            odds.append((M - 1, y))
        
        evens = list()
        for y in range(N):
            evens.append((0, y))
        for x in range(1, M):
            evens.append((x, N - 1))

        L = len(odds)
        starts = list()
        for x in range(L):
            if x % 2 == 0:
                starts.append((odds[x], 1))
            else:
                starts.append((evens[x], -1))

        ans = list()
        for (x, y), dir in starts:
            delta = 0
            while 0 <= x - delta < M and 0 <= y + delta < N:
                ans.append(mat[x - delta][y + delta])
                delta += dir
        return ans


mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2],[3,4]]
mat = [[1,2],[3,4],[5,6]]

solution = Solution()
print(solution.findDiagonalOrder(mat))
