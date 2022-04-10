class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def doValidPalindrome(s, left, right, count):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if count < 1:
                        return doValidPalindrome(s, left + 1, right, count + 1) | doValidPalindrome(s, left, right - 1, count + 1)
                    else:
                        return False

            return True

        return doValidPalindrome(s, 0, len(s) - 1, 0)


s = "aba"
s = "abca"
s = "abc"
s = "cbbcc"

solution = Solution()
print(solution.validPalindrome(s))
