class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        prefix = [[0] * 26 for _ in range(L + 1)]

        for idx, ch in enumerate(s):
            for x in range(26):
                if x == ord(ch) - ord('a'):
                    prefix[idx + 1][x] = prefix[idx][x] + 1
                else:
                    prefix[idx + 1][x] = prefix[idx][x]

        # process
        palindromes = set()
        for x in range(L):
            for y in range(26):
                if prefix[x][y] > 0 and prefix[L][y] - prefix[x + 1][y] > 0:
                    palindrome = chr(ord('a') + y) + s[x] + chr(ord('a') + y)
                    palindromes.add(palindrome)

        ans = len(palindromes)
        print(palindromes)
        return ans


s = "aabca"
s = "adc"
s = "bbcbaba"

solution = Solution()
print(solution.countPalindromicSubsequence(s))
