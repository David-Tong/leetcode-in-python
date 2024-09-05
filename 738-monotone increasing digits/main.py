class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        n = str(n)
        L = len(n)

        # process
        stack = list()
        mono = False
        for digit in n:
            digit = int(digit)
            while stack and stack[-1] > digit:
                mono = True
                digit = stack.pop() - 1
            stack.append(digit)
            if mono:
                stack += [9] * (L - len(stack))
                ans = "".join([str(_) for _ in stack])
                return int(ans)
        return int(n)


n = 10
n = 1234
n = 332
n = 999912240
n = 345321

solution = Solution()
print(solution.monotoneIncreasingDigits(n))
