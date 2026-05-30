class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pre-process
        L = len(s)
        def encrypt(idx):
            target = (idx + k) % L
            return s[target]

        # process
        ans = ""
        idx = 0
        while idx < L:
            ans += encrypt(idx)
            idx += 1
        return ans


s = "dart"
k = 3

s = "aaa"
k = 1

solution = Solution()
print(solution.getEncryptedString(s, k))
