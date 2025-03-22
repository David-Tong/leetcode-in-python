class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)

        # process
        ans = ""
        for x in range(L):
            if x < 2:
                ans += s[x]
            else:
                if s[x] == ans[-1] == ans[-2]:
                    continue
                else:
                    ans += s[x]
        return ans


s = "leeetcode"
s = "aaabaaaa"
s = "aab"
s = "aa"
s = "aaa"

solution = Solution()
print(solution.makeFancyString(s))
