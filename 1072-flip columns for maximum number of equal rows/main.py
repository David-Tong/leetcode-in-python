class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def getEigenValue(row):
            eigen = ""
            for item in row:
                if item == row[0]:
                    eigen += "0"
                else:
                    eigen += "1"
            return eigen

        from collections import defaultdict
        dicts = defaultdict(int)
        for row in matrix:
            eigen = getEigenValue(row)
            dicts[eigen] += 1

        return max(dicts.values())


matrix = [[0,1],[1,1]]
matrix = [[0,1],[1,0]]
matrix = [[0,0,0],[0,0,1],[1,1,0]]

solution = Solution()
print(solution.maxEqualRowsAfterFlips(matrix))
