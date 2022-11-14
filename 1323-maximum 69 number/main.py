class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        for idx, ch in enumerate(s):
            if ch == "6":
                return int(s[:idx] + "9" + s[idx + 1:])
        return num


num = 9669
num = 9996
num = 9999

solution = Solution()
print(solution.maximum69Number(num))
