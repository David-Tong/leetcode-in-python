class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        M = len(mat)

        from collections import defaultdict
        rows = defaultdict(list)
        for row in range(M):
            rows[sum(mat[row])].append(row)

        key = sorted(rows.keys())[-1]
        return [sorted(rows[key])[0], key]


mat = [[0,1],[1,0]]
mat = [[0,0,0],[0,1,1]]
mat = [[0,0],[1,1],[0,0]]

solution = Solution()
print(solution.rowAndMaximumOnes(mat))
