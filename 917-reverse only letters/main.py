class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from string import ascii_lowercase, ascii_uppercase

        L = len(s)
        reversed = ""
        for ch in s[::-1]:
            if ch in ascii_lowercase or ch in ascii_uppercase:
                reversed += ch

        idx = 0
        idx2 = 0
        ans = ""
        while idx < L:
            if s[idx] in ascii_lowercase or s[idx] in ascii_uppercase:
                ans += reversed[idx2]
                idx2 += 1
            else:
                ans += s[idx]
            idx += 1

        return ans


s = "ab-cd"
s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"

solution = Solution()
print(solution.reverseOnlyLetters(s))
