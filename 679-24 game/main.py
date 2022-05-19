class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        self.permutations = []
        self.operators = []

        def doPermutation(cards, selected):
            if len(selected) == 4:
                self.permutations.append(selected[:])
            else:
                for idx, card in enumerate(cards):
                    doPermutation(cards[:idx] + cards[idx+1:], selected[:] + [card])

        def doOperator(selected):
            if len(selected) == 3:
                self.operators.append(selected[:])
            else:
                for operator in ("+", "-", "*", "/"):
                    doOperator(selected[:] + [operator])

        def calculate(suffix):
            stack = []
            for ch in suffix:
                if ch in ("+", "-", "*", "/"):
                    digit2 = float(stack.pop())
                    digit = float(stack.pop())
                    if ch == "+":
                        stack.append(digit + digit2)
                    elif ch == "-":
                        stack.append(digit - digit2)
                    elif ch == "*":
                        stack.append(digit * digit2)
                    elif ch == "/":
                        if digit2 == 0:
                            return -1
                        stack.append(digit / digit2)
                else:
                    stack.append(ch)
            return stack[0]

        doPermutation(cards, [])
        doOperator([])

        suffixes = []
        for permutation in self.permutations:
            for operator in self.operators:
                suffix = permutation + operator
                suffixes.append(suffix)
                suffix = permutation[:2] + [operator[0]] + permutation[2:] + operator[1:]
                suffixes.append(suffix)

        for suffix in suffixes:
            if abs(24 - calculate(suffix)) < 2 ** -10:
                return True
        return False


cards = [4,1,8,7]
#cards = [1,2,1,2]
#cards = [1,9,1,2]
cards = [3,9,7,7]
cards = [8,1,6,6]
cards = [1,1,7,7]
cards = [3,3,8,8]

solution = Solution()
print(solution.judgePoint24(cards))
