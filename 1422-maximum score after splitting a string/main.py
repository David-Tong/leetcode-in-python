class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        left = 1 if s[0] == "0" else 0

        right = 0
        for ch in s[1:]:
            if ch == "1":
                right += 1

        # calculate
        ans = left + right
        for x in range(1, L - 1):
            if s[x] == "0":
                left += 1
            elif s[x] == "1":
                right -= 1
            ans = max(ans, left + right)
        return ans


s = "011101"
s = "00111"
s = "1111"
s = "00000000111111"
s = "10"

solution = Solution()
print(solution.maxScore(s))
