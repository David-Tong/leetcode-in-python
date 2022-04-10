class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        ans = 0
        carry = 0
        for ch in dicts.keys():
            if dicts[ch] % 2 == 1:
                carry = 1
            if dicts[ch] % 2 == 1:
                ans += dicts[ch] - 1
            else:
                ans += dicts[ch]
        ans += carry
        return ans


s = "abccccdd"
#s = "aa"
#s = "b"
#s = "ccb"
#s = "ccc"

solution = Solution()
print(solution.longestPalindrome(s))
