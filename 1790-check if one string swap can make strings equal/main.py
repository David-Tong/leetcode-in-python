class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = []
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                count.append(x)
        if len(count) == 0:
            return True
        elif len(count) == 2:
            if s1[count[0]] == s2[count[1]] and s1[count[1]] == s2[count[0]]:
                return True
            else:
                return False
        else:
            return False


s1 = "bank"
s2 = "kanb"

#s1 = "attack"
#s2 = "defend"

#s1 = "kelb"
#s2 = "kelb"

#s1 = "caa"
#s2 = "aaz"

#s1 = "aa"
#s2 = "ac"

solution = Solution()
print(solution.areAlmostEqual(s1, s2))
