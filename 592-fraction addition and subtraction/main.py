class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # lcd
        def lcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # pre-process
        L = len(expression)
        signals = list()
        if expression[0] != "-":
            expression = "+" + expression
            L += 1
        for idx, ch in enumerate(expression):
            if ch == "+" or ch == "-":
                signals.append(idx)
        signals.append(L)
        # print(signals)

        numerators = list()
        denominators = list()
        for x in range(len(signals) - 1):
            fraction = expression[signals[x] + 1:signals[x + 1]]
            signal = expression[signals[x]]
            numerator, denominator = fraction.split('/')
            if signal == "+":
                numerators.append(int(numerator))
                denominators.append(int(denominator))
            elif signal == "-":
                numerators.append(-1 * int(numerator))
                denominators.append(int(denominator))
        # print(numerators, denominators)

        # process
        numerator = 0
        for x in range(len(numerators)):
            part_numerator = numerators[x]
            for y in range(len(denominators)):
                if x != y:
                    part_numerator *= denominators[y]
            numerator += part_numerator

        denominator = 1
        for y in range(len(denominators)):
            denominator *= denominators[y]

        # post-process
        l = lcd(abs(numerator), abs(denominator))
        numerator = numerator // l
        denominator = denominator // l
        ans = str(numerator) + "/" + str(denominator)
        return ans


expression = "-1/2+1/2"
expression = "-1/2+1/2+1/3"
expression = "1/3-1/2"
expression = "-1/20+1/12+1/3"
expression = "0/10-20/1+13/28"

solution = Solution()
print(solution.fractionAddition(expression))