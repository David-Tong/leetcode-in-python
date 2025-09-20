class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # pre-process
        from collections import defaultdict
        words = sorted(words, key=lambda x:len(x))
        dicts = defaultdict(dict)
        for word in words:
            for ch in word:
                if ch not in dicts[word]:
                    dicts[word][ch] = 0
                dicts[word][ch] += 1

        import string
        from collections import defaultdict
        chs = defaultdict(int)
        for ch in licensePlate:
            if ch in string.ascii_letters:
                chs[ch.lower()] += 1

        # process
        for word in words:
            match = True
            for ch in chs:
                if ch in dicts[word]:
                    if dicts[word][ch] >= chs[ch]:
                        pass
                    else:
                        match = False
                        break
                else:
                    match = False
                    break
            if match:
                return word


licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]

licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]

solution = Solution()
print(solution.shortestCompletingWord(licensePlate, words))
