class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)
        if L <= 2:
            return s

        # process
        start = 0
        diff = 0
        idx = 0
        substrings = list()
        while idx < L:
            if s[idx] == "1":
                diff += 1
            else:
                diff -= 1
                if diff == 0:
                    substrings.append("1{}0".format(self.makeLargestSpecial(s[start + 1: idx])))
                    start = idx + 1
            idx += 1
        substrings.sort(reverse=True)
        ans = "".join(substrings)
        return ans


s = "11011000"
s = "10"

solution = Solution()
print(solution.makeLargestSpecial(s))
