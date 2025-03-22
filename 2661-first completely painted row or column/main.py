class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])
        from collections import defaultdict
        dicts = defaultdict(set)
        for x in range(M):
            for y in range(N):
                dicts[mat[x][y]] = (x, y)
        rows = [0] * M
        cols = [0] * N

        # process
        for idx, item in enumerate(arr):
            x, y = dicts[item]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == N or cols[y] == M:
                return idx


arr = [1,3,4,2]
mat = [[1,4],[2,3]]

arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]

solution = Solution()
print(solution.firstCompleteIndex(arr, mat))
