class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # pre-process
        def change(s):
            res = ""
            for ch in s:
                res += chr(ord('a') + (ord(ch) - ord('a') + 1) % 26)
            return res

        # process
        s = "a"
        while len(s) <= k:
            s += change(s)
        # print(s)
        ans = s[k - 1]
        return ans


k = 5
k = 10
k = 500

solution = Solution()
print(solution.kthCharacter(k))
