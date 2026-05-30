class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])

        # process
        shifted = [[0] * N for _ in range(M)]
        for x in range(M):
            if x % 2 == 0:
                start = N - k % N
            else:
                start = k % N
            for y in range(N):
                idx = (start + y) % N
                shifted[x][idx] = mat[x][y]

        # post-process
        for x in range(M):
            for y in range(N):
                if shifted[x][y] != mat[x][y]:
                    return False
        return True


mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 4

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2

mat = [[2,2],[2,2]]
k = 3

solution = Solution()
print(solution.areSimilar(mat, k))
