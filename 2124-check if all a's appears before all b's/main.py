class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx_a = -1
        idx_b = -1

        for idx, ch in enumerate(s):
            if ch == "a":
                idx_a = idx
            elif idx_b == -1 and ch == "b":
                idx_b = idx

        if idx_a == -1 or idx_b == -1:
            return True

        if idx_a < idx_b:
            return True
        else:
            return False


s = "aaabbb"
s = "abab"
s = "bbb"
s = "aa"

solution = Solution()
print(solution.checkString(s))
