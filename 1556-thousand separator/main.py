class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        # pre-process
        num = str(n)
        L = len(num)

        # process
        idx = L - 1
        count = 1
        ans = list()
        while idx >= 0:
            ans.append(num[idx])
            if count % 3 == 0:
                if idx != 0:
                    ans.append(".")
            count += 1
            idx -= 1
        ans = "".join(reversed(ans))
        return ans


n = 987
n = 1234

solution = Solution()
print(solution.thousandSeparator(n))
