class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        if len(needle) == 0:
            return 0

        for idx in range(len(haystack)):
            idx2 = 0
            while idx < len(haystack) and idx2 < len(needle):
                if haystack[idx] == needle[idx2]:
                    idx2 += 1
                else:
                    break
                idx += 1

                if idx2 == len(needle):
                    return idx - idx2

        return -1


haystack = "hello"
needle = "ll"

haystack = "aaaaa"
needle = "bba"

haystack = "aaaaabb"
needle = "bba"

haystack = "mississippi"
needle = "issip"

haystack = "aabaabbbaabbbbabaaab"
needle = "abaa"

solution = Solution()
print(solution.strStr(haystack, needle))
