class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        M = len(mat)

        # get the max value in a row
        def getPeakRowCol(target):
            row = mat[target]
            peak_idx = 0
            peak_val = row[0]
            for idx, val in enumerate(row):
                if val > peak_val:
                    peak_idx = idx
                    peak_val = val
            return peak_idx, peak_val

        # check if this item is peak in a column for its adjacent cells
        def isPeakInCol(row, col):
            if row > 0:
                if mat[row][col] < mat[row - 1][col]:
                    return False
            if row < M - 1:
                if mat[row][col] < mat[row + 1][col]:
                    return False
            return True

        # binary search row
        low = 0
        high = M - 1
        while low + 1 < high:
            middle = (low + high) // 2
            idx, _ = getPeakRowCol(middle)
            if mat[middle][idx] > mat[middle - 1][idx]:
                if mat[middle][idx] > mat[middle + 1][idx]:
                    return [middle, idx]
                else:
                    low = middle + 1
            else:
                high = middle - 1

        # check low
        idx, _ = getPeakRowCol(low)
        if isPeakInCol(low, idx):
            return [low, idx]

        # check high
        idx, _ = getPeakRowCol(high)
        if isPeakInCol(high, idx):
            return [high, idx]


mat = [[1,4],[3,2]]
mat = [[10,20,15],[21,30,14],[7,16,32]]
mat = [[1,2]]
mat = [[1]]

solution = Solution()
print(solution.findPeakGrid(mat))
