class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = []
        operators = []

        # process "-" as a unary operation
        if s[0] == "-":
            s = "0" + s
        for x in range(len(s)):
            if s[x] == "(" and s[x+1] == "-":
                s = s[:x+1] + "0" + s[x+1:]

        # build suffix expr
        slow = 0
        fast = 0
        is_digital = False
        while fast < len(s):
            if s[fast] in ("+", "-", "(", ")", " "):
                if is_digital:
                    digits.append(s[slow:fast])
                is_digital = False
                if s[fast] in ("+", "-", "("):
                    if s[fast] in ("+", "-"):
                        while operators and operators[-1] in ("+", "-"):
                            operator = operators.pop()
                            digits.append(operator)
                    operators.append(s[fast])
                elif s[fast] == ")":
                    while operators:
                        operator = operators.pop()
                        if operator == "(":
                            break
                        else:
                            digits.append(operator)
            else:
                if not is_digital:
                    slow = fast
                is_digital = True
            fast += 1

        if is_digital:
            digits.append(s[slow:fast])

        while operators:
            operator = operators.pop()
            digits.append(operator)

        # calculate
        stack = []
        for ch in digits:
            if ch == "+" or ch == "-":
                digit2 = int(stack.pop())
                digit = int(stack.pop())
                if ch == "+":
                    stack.append(digit + digit2)
                elif ch == "-":
                    stack.append(digit - digit2)
            else:
                stack.append(ch)
        return stack[0]

s = "1 + 1"
s = " 2-1 + 2 "
s = "(1+(4+5+2)-3)+(6+8)"
s = "-6+(1+(-45+52+2)-3)+(16+8)"

solution = Solution()
print(solution.calculate(s))
