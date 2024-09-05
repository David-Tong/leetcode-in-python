import string


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # pre-process
        L = len(words)
        from collections import defaultdict
        dicts = defaultdict(list)

        # process
        for word in words:
            ones = defaultdict(int)
            for ch in word:
                ones[ch] += 1
            for ch in ones:
                dicts[ch].append(ones[ch])

        ans = list()
        for ch in dicts:
            if len(dicts[ch]) == L:
                for _ in range(min(dicts[ch])):
                    ans.append(ch)
        return ans


words = ["bella","label","roller"]
words = ["cool","lock","cook"]
words = ["ooo", "oooo", "roookie"]

solution = Solution()
print(solution.commonChars(words))
