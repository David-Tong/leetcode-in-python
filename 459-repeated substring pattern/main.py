class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)
        for x in range(L // 2):
            if L % (x + 1) == 0:
                repeat = L // (x + 1)
                print(s[:x + 1])
                if s[:x + 1] * repeat == s:
                    return True
        return False


s = "abab"
s = "aba"
#s = "abcabcabcabc"
#s = "abcabcabc"

solution = Solution()
print(solution.repeatedSubstringPattern(s))
