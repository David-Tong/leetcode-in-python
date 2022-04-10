class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[0::2] + s[1::2]

        numCols = len(s)
        array = [[""] * numCols for x in range(numRows)]
        row = 0
        col = 0
        for ch in s:
            if row == 0:
                zig = True
                zag = False
            elif row == numRows:
                zig = False
                zag = True
                row -= 2
                col += 1

            if zig:
                array[row][col] = ch
                row += 1
            elif zag:
                array[row][col] = ch
                row -= 1
                col += 1

        ans = ""
        for x in range(len(array)):
            for y in range(len(array[0])):
                if array[x][y] != "":
                    ans += array[x][y]
        return ans


s = "PAYPALISHIRING"
numRows = 3

s = "PAYPALISHIRING"
numRows = 4

s = "A"
numRows = 1

s = "ABCDEF"
numRows = 2

solution = Solution()
print(solution.convert(s, numRows))
