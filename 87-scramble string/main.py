class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def canScramble(s1, s2):
            key = s1 + "_" + s2
            if key in cache:
                return cache[key]

            if s1 == s2:
                return True

            if len(s1) != len(s2):
                return False

            if sorted(s1) != sorted(s2):
                return False

            L = len(s1)

            for x in range(1, L):
                s11 = s1[:x]
                s12 = s1[x:]
                s21 = s2[:x]
                s22 = s2[x:]
                if canScramble(s11, s21) and canScramble(s12, s22):
                    cache[key] = True
                    return True
                s21 = s2[L - x:]
                s22 = s2[:L - x]
                if canScramble(s11, s21) and canScramble(s12, s22):
                    cache[key] = True
                    return True

            cache[key] = False
            return False

        if len(s1) == 0 or len(s2) == 0:
            if len(s1) == len(s2):
                return True
            else:
                return False

        from collections import defaultdict
        cache = defaultdict(str)

        return canScramble(s1, s2)


s1 = "great"
s2 = "rgeat"

s1 = "abcde"
s2 = "caebd"

s1 = "a"
s2 = "a"

s1 = "abcdbdacbdac"
s2 = "bdacabcdbdac"

s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"

solution = Solution()
print(solution.isScramble(s1, s2))
