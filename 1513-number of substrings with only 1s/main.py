class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        L = len(s)

        def countSub(n):
            return (n * (n + 1) // 2) % MODULO

        inOnes = False
        startOnes = -1
        idx = 0

        ans = 0
        while idx < L:
            if s[idx] == "0":
                if inOnes:
                    inOnes = False
                    ones = idx - startOnes
                    ans += countSub(ones)
            elif s[idx] == "1":
                if not inOnes:
                    inOnes = True
                    startOnes = idx
            idx += 1

        if inOnes:
            ones = idx - startOnes
            ans += countSub(ones)

        return ans


s = "0110111"
s = "101"
s = "111111"
s = "00000"
s = "0"
s = "1" * 10 ** 3
print(s)

solution = Solution()
print(solution.numSub(s))
