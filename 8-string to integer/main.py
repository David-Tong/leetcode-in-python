class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        start = 0
        for idx, ch in enumerate(s):
            if ch == "+" or ch == "-" or \
                ord(ch) >= 49 and ord(ch) <= 57:
                start = idx
                break

        end = len(s)
        for idx, ch in enumerate(s[start+1:]):
            if ch == "." or ch == "+" or ch == "-":
                end = start + idx + 1
                break

        zeros = False
        for ch in s[:start]:
            if ch == " ":
                if zeros:
                    return 0
            elif ch == "0":
                zeros = True
                continue
            else:
                return 0

        negative = False
        ans = 0
        left = start
        right = end
        for idx, ch in enumerate(s[start:end]):
            if ch == "+" or ch == "-":
                if start + idx + 1 >= end:
                    return 0
                else:
                    if ord(s[start+idx+1]) < 48 or ord(s[start+idx+1]) > 57:
                        return 0
                if ch == "-":
                    negative = True
                    if start != 0:
                        if zeros:
                            return 0
                left = start + idx + 1
            elif ord(s[start+idx]) < 48 or ord(s[start+idx]) > 57:
                right = start + idx
                break

        if right - left >= 1:
            ans = int(s[left:right])

        if negative:
            ans = -1 * ans
        if ans < -1 * 2 ** 31:
            ans = -1 * 2 ** 31
        elif ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        return ans


str = "42"
#str = "-42"
#str = "4193 with words"
str = "words and 987"
str = "-91283472332"
str = ".1"
str = "+"
str = "+-2"
str = "-   234"
str = "   -42"
str = "3.1415926"
str = "+-12"
str = ""
str = "+"
str = "21474836460"
str = "00000-42a1234"
#str = "-000000000000001"
#str = "0-1"
#str = "   -42"
#str = "0  123"
#str = "-5-"
str = "21474836++"

solution = Solution()
print(solution.myAtoi(str))
