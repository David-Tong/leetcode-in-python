class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        # pre-process
        L, L2 = len(str1), len(str2)

        # process
        idx, idx2 = 0, 0
        while idx < L and idx2 < L2:
            ch = str1[idx]
            ich = chr(ord('a') + (ord(ch) - ord('a') + 1) % 26)
            if ch == str2[idx2] or ich == str2[idx2]:
                idx2 += 1
            idx += 1

        return True if idx2 == L2 else False


str1 = "abc"
str2 = "ad"

str1 = "zc"
str2 = "ad"

str1 = "ab"
str2 = "d"

solution = Solution()
print(solution.canMakeSubsequence(str1, str2))
