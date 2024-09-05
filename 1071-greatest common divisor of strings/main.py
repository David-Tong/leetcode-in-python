class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def getGCDs(astr):
            L = len(astr)
            gcds = set()
            gcds.add(astr)

            for x in range(L // 2):
                gcd = astr[:x + 1]
                if L % (x + 1) == 0:
                    t = L // (x + 1)
                    if gcd * t == astr:
                        gcds.add(gcd)

            return gcds

        gcds1 = getGCDs(str1)
        gcds2 = getGCDs(str2)
        gcds = gcds1 & gcds2

        ans = ""
        for gcd in gcds:
            if len(gcd) > len(ans):
                ans = gcd
        return ans


str1 = "ABCABC"
str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

str1 = "LEET"
str2 = "CODE"

solution = Solution()
print(solution.gcdOfStrings(str1, str2))
