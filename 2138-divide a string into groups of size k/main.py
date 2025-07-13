class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        # pre-process
        L = len(s)

        # process
        idx = 0
        ss = ""
        ans = list()
        while idx < L:
            ss += s[idx]
            idx += 1
            if idx % k == 0:
                ans.append(ss)
                ss = ""

        if idx % k != 0:
            remain = k - idx % k
            ans.append(ss + fill * remain)
        return ans


s = "abcdefghi"
k = 3
fill = "x"

s = "abcdefghij"
k = 3
fill = "x"

solution = Solution()
print(solution.divideString(s, k, fill))
