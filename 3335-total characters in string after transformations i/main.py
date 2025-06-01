class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        MOD = 26
        L = len(s)
        chs = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            chs[idx] += 1

        # process
        def getPivot(idx):
            return (idx + MOD) % MOD

        idx = 25
        ans = L
        for _ in range(t):
            chs[getPivot(idx + 1)] += chs[getPivot(idx)]
            ans = (ans + chs[getPivot(idx)]) % MODULO
            idx -= 1
            if idx < 0:
                idx += MOD
        return ans % MODULO


s = "abcyy"
t = 2

s = "azbk"
t = 1

s = "aaaaaa"
t = 1000

solution = Solution()
print(solution.lengthAfterTransformations(s, t))
