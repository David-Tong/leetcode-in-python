class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process
        while len(s) > 2:
            ns = ""
            idx = 1
            while idx < len(s):
                mod = (int(s[idx - 1]) + int(s[idx])) % 10
                ns += str(mod)
                idx += 1
            s = ns
        return s[0] == s[1]


s = "3902"
s = "34789"

solution = Solution()
print(solution.hasSameDigits(s))
