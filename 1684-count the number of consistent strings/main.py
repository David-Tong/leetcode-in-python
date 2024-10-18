class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # pre-process
        allows = set()
        for _ in allowed:
            allows.add(_)

        # process
        ans = 0
        for word in words:
            consistent = True
            for c in word:
                if c not in allows:
                    consistent = False
                    break
            if consistent:
                ans += 1
        return ans


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]

solution = Solution()
print(solution.countConsistentStrings(allowed, words))
