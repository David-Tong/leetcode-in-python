class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        # pre-process
        L = len(pref)

        # process
        ans = 0
        for word in words:
            if word[:L] == pref:
                ans += 1
        return ans


words = ["pay","attention","practice","attend"]
pref = "at"

words = ["leetcode","win","loops","success"]
pref = "code"

solution = Solution()
print(solution.prefixCount(words, pref))
