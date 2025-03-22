class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a != b:
            return max(len(a), len(b))
        else:
            return -1

a = "aba"
b = "cdc"

a = "aaa"
b = "bbb"

a = "aaa"
b = "aaa"

a = "aaajgf"
b = "aajgf"

a = "abc"
b = "abcdef"

solution = Solution()
print(solution.findLUSlength(a, b))
