class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # pre-process
        L = len(words[0])

        # helper function
        def getKey(word):
            diffs = list()
            idx = 0
            while idx < L - 1:
                diffs.append(str(ord(word[idx + 1]) - ord(word[idx])))
                idx += 1
            res = "|".join(diffs)
            return res

        # process
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, word in enumerate(words):
            key = getKey(word)
            dicts[key].append(idx)

        # post-process
        for key in dicts:
            if len(dicts[key]) == 1:
                idx = dicts[key][0]
                break
        ans = words[idx]
        return ans


words = ["adc","wzy","abc"]
words = ["aaa","bob","ccc","ddd"]

solution = Solution()
print(solution.oddString(words))

