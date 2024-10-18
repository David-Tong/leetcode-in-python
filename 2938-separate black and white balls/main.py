class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        slow, fast = 0, 0

        # process
        ans = 0
        while fast < L:
            if s[fast] == '0':
                ans += fast - slow
                slow += 1
            fast += 1
        return ans


s = "101"
s = "100"
s = "0111"
s = "0011010101010111"
s = "1"

solution = Solution()
print(solution.minimumSteps(s))
