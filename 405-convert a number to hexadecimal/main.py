class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # pre-process
        digits = list()
        for x in range(31):
            digits.append(abs(num) >> x & 1)

        if num < 0:
            # get ones' complement
            digits = [1 - x for x in digits]
            # get two's complement
            addon = 1
            for x in range(31):
                result = (digits[x] + addon) % 2
                addon = (digits[x] + addon) // 2
                digits[x] = result
            digits.append(1)
        else:
            digits.append(0)

        # process
        ans = ""
        for x in range(0, 32, 4):
            hex = digits[x: x+ 4]
            number = 0
            for y in range(4):
                number += hex[y] * 2 ** y
            if number < 10:
                ans = str(number) + ans
            else:
                ans = chr(ord('a') + number - 10) + ans

        # remove leading zeros
        idx = 0
        for x in range(len(ans)):
            if ans[x] == "0":
                idx += 1
            else:
                break
        if idx == len(ans):
            return "0"
        else:
            return ans[idx:]


num = 26
num = -1
num = 0
num = -1 * 2 ** 31
num = 2 ** 31 - 1

solution = Solution()
print(solution.toHex(num))
