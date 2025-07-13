class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pre-process
        L = len(s)

        # process
        idx = 0
        ans = ""
        while idx < L:
            ans += s[idx: idx + k][::-1] + s[idx + k: idx + 2 * k]
            idx += 2 * k
        return ans


s = "abcdefg"
k = 2

s = "abcd"
k = 2

s = "abcdefgh"
k = 3

s = "abcdefghijklm"
k = 3

solution = Solution()
print(solution.reverseStr(s, k))
