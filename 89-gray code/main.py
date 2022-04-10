class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def doGrayCode(n):
            if n == 1:
                return ["0", "1"]
            else:
                ans = []
                codes = doGrayCode(n - 1)
                for code in codes:
                    ans.append("0" + code)
                for code in codes[::-1]:
                    ans.append("1" + code)
                return ans

        ans = doGrayCode(n)
        ans = [int(_, 2) for _ in ans]
        return ans


n = 1
n = 2
n = 16

solution = Solution()
print(solution.grayCode(n))
