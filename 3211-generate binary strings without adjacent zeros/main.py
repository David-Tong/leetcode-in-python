class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # process
        ans = list()

        def make(idx, s):
            if idx == n:
                ans.append(s)
                return
            if idx > 0:
                if s[-1] == "0":
                    make(idx + 1, s + "1")
                    return
            make(idx + 1, s + "0")
            make(idx + 1, s + "1")

        make(0, "")
        return ans


n = 3
n = 1
n = 18

solution = Solution()
print(solution.validStrings(n))
