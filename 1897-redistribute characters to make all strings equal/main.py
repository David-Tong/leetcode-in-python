class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        # pre-process
        L = len(words)
        if L == 1:
            return True

        from collections import defaultdict
        dicts = defaultdict(int)

        for word in words:
            for ch in word:
                dicts[ch] += 1

        # process
        for ch in dicts:
            if dicts[ch] % L != 0:
                return False
        return True


words = ["abc","aabc","bc"]
words = ["ab","a"]
words = ["b"]

solution = Solution()
print(solution.makeEqual(words))
