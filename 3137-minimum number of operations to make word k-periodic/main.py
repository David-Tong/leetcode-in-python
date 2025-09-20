class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(word)
        from collections import defaultdict
        dicts = defaultdict(int)
        for x in range(0, L, k):
            key = word[x: x + k]
            dicts[key] += 1

        # process
        ans = L // k - max(dicts.values())
        return ans


word = "leetcodeleet"
k = 4

word = "leetcoleet"
k = 2

solution = Solution()
print(solution.minimumOperationsToMakeKPeriodic(word, k))
