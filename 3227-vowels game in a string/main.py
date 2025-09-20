class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # pre-process
        VOWELS = "aeiou"
        vowel = 0
        for ch in s:
            if ch in VOWELS:
                vowel += 1

        # process
        return True if vowel > 0 else False


s = "leetcoder"
s = "bbcd"
s = "laabodd"

solution = Solution()
print(solution.doesAliceWin(s))
