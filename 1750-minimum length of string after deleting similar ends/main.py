class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        left = 0
        right = L - 1

        # process
        while left < right:
            if s[left] == s[right]:
                idx = 1
                while left + idx < L and s[left + idx] == s[left]:
                    idx += 1
                left = left + idx
                idx = 1
                while right - idx >= 0 and s[right - idx] == s[right]:
                    idx += 1
                right = right - idx
            else:
                return right - left + 1

        if left <= right:
            return right - left + 1
        else:
            return 0


s = "ca"
s = "cabaabac"
s = "aabccabba"
s = "cabababac"
s = "cabaaabac"
s = "bbb"
s = "bbbbbbbbbbbbbbbbbbb"

solution = Solution()
print(solution.minimumLength(s))
