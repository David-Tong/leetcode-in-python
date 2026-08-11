class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        num = ""
        num2 = 0
        zeros = 0
        s = str(n)
        for ch in s:
            if ch != "0":
                num += ch
                num2 += int(ch)
            else:
                zeros += 1

        # process
        num = 0 if num == "" else int(num)
        ans = num * num2
        return ans


n = 10203004
n = 1000
n = 12345
n = 0

solution = Solution()
print(solution.sumAndMultiply(n))
