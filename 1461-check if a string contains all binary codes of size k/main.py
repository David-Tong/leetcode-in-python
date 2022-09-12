class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        def calcRollingHash(hashing, obit, ibit, k):
            hashing -= int(obit) * 2 ** (k - 1)
            hashing *= 2
            hashing += int(ibit)
            return hashing

        def calcHash(s, k):
            hashing = 0
            for x in range(k):
                hashing += int(s[x]) * 2 ** (k - 1 - x)
            return hashing

        L = len(s)
        if 2 ** k > L - k + 1:
            return False

        from collections import defaultdict
        dicts = defaultdict(int)
        count = 0
        hashing = 0
        for x in range(L - k + 1):
            if x == 0:
                hashing = calcHash(s[x:x+k], k)
            else:
                hashing = calcRollingHash(hashing, s[x-1], s[x+k-1], k)

            if hashing not in dicts:
                dicts[hashing] = 1
                count += 1

        if count == 2 ** k:
            return True
        else:
            return False


s = "00110110"
k = 2

s = "0110"
k = 1

s = "0110"
k = 2

s = "00"
k = 0

solution = Solution()
print(solution.hasAllCodes(s, k))
