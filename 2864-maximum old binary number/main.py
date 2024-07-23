class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)
        evens, odds = 0, 0
        for ch in s:
            if ch == "1":
                odds += 1
            else:
                evens += 1

        # process
        ans = "1" * (odds - 1) + "0" * evens + "1"
        return ans


s = "010"
s = "0101"

solution = Solution()
print(solution.maximumOddBinaryNumber(s))
