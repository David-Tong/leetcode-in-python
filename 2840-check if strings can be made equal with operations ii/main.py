class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # pre-process
        from collections import defaultdict
        evens_s1, evens_s2 = defaultdict(int), defaultdict(int)
        odds_s1, odds_s2 = defaultdict(int), defaultdict(int)

        for idx, ch in enumerate(s1):
            if idx % 2 == 0:
                evens_s1[ch] += 1
            else:
                odds_s1[ch] += 1

        for idx, ch in enumerate(s2):
            if idx % 2 == 0:
                evens_s2[ch] += 1
            else:
                odds_s2[ch] += 1

        # process
        for ch in evens_s1:
            if evens_s1[ch] != evens_s2[ch]:
                return False

        for ch in odds_s1:
            if odds_s1[ch] != odds_s2[ch]:
                return False

        return True


s1 = "abcdba"
s2 = "cabdab"

s1 = "abe"
s2 = "bea"

solution = Solution()
print(solution.checkStrings(s1, s2))
