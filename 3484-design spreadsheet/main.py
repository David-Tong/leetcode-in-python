class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        from collections import defaultdict
        self.dicts = defaultdict(int)

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.dicts[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        if cell in self.dicts:
            del self.dicts[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        res = 0
        operand, operand2 = formula[1:].split("+")
        if operand.isdigit():
            res += int(operand)
        else:
            if operand in self.dicts:
                res += self.dicts[operand]
        if operand2.isdigit():
            res += int(operand2)
        else:
            if operand2 in self.dicts:
                res += self.dicts[operand2]
        return res


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

"""
ss = Spreadsheet(3)
print(ss.getValue("=5+7"))
ss.setCell("A1", 10)
print(ss.getValue("=A1+6"))
ss.setCell("B2", 15)
print(ss.getValue("=A1+B2"))
ss.resetCell("A1")
print(ss.getValue("=A1+B2"))
"""

ss = Spreadsheet(24)
ss.setCell("B24", 66688)
ss.resetCell("015")