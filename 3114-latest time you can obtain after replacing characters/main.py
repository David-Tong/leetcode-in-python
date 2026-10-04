class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)

        # process
        ans = list()

        idx = 0
        while idx < L:
            ch = s[idx]
            if ch == "?":
                if idx == 0:
                    if s[idx + 1] == "0" or s[idx + 1] == "1" or s[idx + 1] == "?":
                        ans.append("1")
                    else:
                        ans.append("0")
                elif idx == 1:
                    if ans[idx - 1] == "1":
                        ans.append("1")
                    else:
                        ans.append("9")
                elif idx == 3:
                    ans.append("5")
                elif idx == 4:
                    ans.append("9")
            else:
                ans.append(ch)
            idx += 1
        ans = "".join(ans)
        return ans


s = "1?:?4"
s = "0?:5?"
s = "?3:12"

solution = Solution()
print(solution.findLatestTime(s))
