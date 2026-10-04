class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        # pre-process
        L = len(a)

        # helper function
        def check(s):
            if L % 2 == 0:
                left, right = L // 2 - 1, L // 2
            else:
                left, right = L // 2, L // 2

            while left >= 0 and right < L and s[left] == s[right]:
                left -= 1
                right += 1

            return left

        # process
        # case 1 : a as the palindrome middle
        limit = check(a)
        idx = 0
        palindrome = [True] * 2
        while idx <= limit:
            if a[idx] != b[L - 1 - idx]:
                palindrome[0] = False
            if b[idx] != a[L - 1 - idx]:
                palindrome[1] = False
            idx += 1

        if palindrome[0] or palindrome[1]:
            return True

        # case 2 : b as the palindrom middle
        limit = check(b)
        idx = 0
        palindrome = [True] * 2
        while idx <= limit:
            if a[idx] != b[L - 1 - idx]:
                palindrome[0] = False
            if b[idx] != a[L - 1 - idx]:
                palindrome[1] = False
            idx += 1

        if palindrome[0] or palindrome[1]:
            return True

        return False


a = "x"
b = "y"

a = "xbdef"
b = "xecab"

a = "ulacfd"
b = "jizalu"

a = "pvhmupgqeltozftlmfjjde"
b = "yjgpzbezspnnpszebzmhvp"

a = "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
b = "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"

solution = Solution()
print(solution.checkPalindromeFormation(a, b))
