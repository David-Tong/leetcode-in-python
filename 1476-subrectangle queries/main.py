class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rows = len(rectangle)
        self.cols = len(rectangle[0])
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for x in range(row1, row2 + 1):
            for y in range(col1, col2 + 1):
                self.rectangle[x][y] = newValue

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
srq = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(srq.getValue(0, 2))
srq.updateSubrectangle(0,0,3,2,5)
print(srq.getValue(0, 2))
print(srq.getValue(3, 1))
srq.updateSubrectangle(3,0,3,2,10)
print(srq.getValue(3, 1))
print(srq.getValue(0, 2))
