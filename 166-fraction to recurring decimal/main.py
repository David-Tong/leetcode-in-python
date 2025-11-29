class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # handle signal
        signal = ""
        if numerator * denominator < 0:
            signal = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        from collections import defaultdict
        numerators = defaultdict(int)
        quotients = list()

        integer = "0"
        if numerator >= denominator:
            integer = str(numerator // denominator)
            numerator = numerator % denominator

        repeating = True
        if numerator > 0:
            idx = 0
            while numerator not in numerators:
                numerators[numerator] = idx
                factor = 0
                while numerator < denominator:
                    numerator = numerator * 10
                    factor += 1

                # handle quotient
                quotient = numerator // denominator
                quotient = "0" * (factor - 1) + str(quotient)
                quotients.append(quotient)

                # handle remainder
                remainder = numerator % denominator
                if remainder == 0:
                    repeating = False
                    break

                numerator = remainder
                idx += 1

            decimal = "."
            for idx, quotient in enumerate(quotients):
                if repeating and numerators[numerator] == idx:
                    decimal += "("
                decimal += str(quotient)
            if repeating:
                decimal += ")"

            return signal + integer + decimal
        else:
            return signal + integer


numerator = 1
denominator = 2

numerator = 2
denominator = 1

numerator = 4
denominator = 9

numerator = 35
denominator = 1983

numerator = -50
denominator = 8

numerator = 4
denominator = 333

numerator = 1
denominator = 214748364

numerator = 1
denominator = -1

solution = Solution()
print(solution.fractionToDecimal(numerator, denominator))
