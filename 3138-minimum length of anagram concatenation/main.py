class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        from math import sqrt
        ks = set()
        for x in range(1, int(sqrt(L)) + 1):
            if L % x == 0:
                ks.add(x)
                ks.add(L // x)
        ks = sorted(list(ks))

        presum = [[0] * 26 for _ in range(L + 1)]
        for idx, ch in enumerate(s):
            for x in range(26):
                presum[idx + 1][x] = presum[idx][x]
            presum[idx + 1][ord(ch) - ord('a')] += 1

        # process
        # check - check if s is k folds anagram concatenation
        def check(k):
            factor = L // k
            for c in range(26):
                if presum[-1][c] % factor != 0:
                    return False

            for x in range(2 * k, L + 1, k):
                for c in range(26):
                    if presum[x][c] - presum[x - k][c] != presum[k][c]:
                        return False
            return True

        for k in ks:
            if check(k):
                return k
        return L


s = "abba"
s = "cdef"
s = "abcbcacabbaccba"
s = "aaccaaacacaaaca"
s = "aaaaaaaaaa"
s = "aabb"

solution = Solution()
print(solution.minAnagramLength(s))
