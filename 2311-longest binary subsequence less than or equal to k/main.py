class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(s)
        ones, zeros = list(), 0
        for idx, ch in enumerate(s):
            if ch == "1":
                ones.append(L - 1 - idx)
            elif ch == "0":
                zeros += 1
        ones = sorted(ones)

        # process
        ans = zeros
        value = 0
        for one in ones:
            value += 2 ** one
            if value <= k:
                ans += 1
            else:
                return ans
        return ans


s = "1001010"
k = 5

s = "00101001"
k = 1

s = "010100101100101111011001111"
k = 1000

solution = Solution()
print(solution.longestSubsequence(s, k))
