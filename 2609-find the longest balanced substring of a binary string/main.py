class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def hasSubstring(target):
            substring = "0" * target + "1" * target
            if substring in s:
                return True
            else:
                return False

        left = 0
        right = len(s) // 2

        while left + 1 < right:
            middle = (left + right) // 2
            if hasSubstring(middle):
                left = middle
            else:
                right = middle - 1

        if hasSubstring(right):
            return right * 2
        else:
            return left * 2


s = "01000111"
s = "00111"
s = "111"
s = "0"
s = "00000000000001111111111111111"

solution = Solution()
print(solution.findTheLongestBalancedSubstring(s))
