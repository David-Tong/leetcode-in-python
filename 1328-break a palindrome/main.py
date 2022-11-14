class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        L = len(palindrome)
        if L % 2 == 1:
            M = L / 2
        else:
            M = -1

        if L == 1:
            return ""

        for idx, ch in enumerate(palindrome):
            if ch != "a":
                if idx != M:
                    return palindrome[:idx] + "a" + palindrome[idx + 1:]
            if idx == L - 1:
                return palindrome[:idx] + "b"


palindrome = "abccba"
palindrome = "a"
palindrome = "aaaa"
palindrome = "bb"
palindrome = "aba"


solution = Solution()
print(solution.breakPalindrome(palindrome))
