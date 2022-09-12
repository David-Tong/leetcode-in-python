class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return 2
        return 1


s = "ababa"
s = "abb"
s = "baabb"
s = "bbaabaaa"

solution = Solution()
print(solution.removePalindromeSub(s))
