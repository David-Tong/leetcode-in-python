class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.anses = []

        def doOperate(num, target, expr, operator):
            # stop recursion
            if len(num) == 0:
                if eval(expr) == target:
                    self.anses.append(expr)
                return

            # add operator
            if operator:
                for oper in ("+", "-", "*"):
                    doOperate(num[:], target, expr + oper, not operator)
            else:
                # add numbers
                for x in range(len(num)):
                    number = num[:x+1]
                    # filter all number like "0xxx"
                    if number[0] == "0" and len(number) > 1:
                        continue
                    doOperate(num[x+1:], target, expr + number, not operator)

        doOperate(num, target, "", False)
        return self.anses