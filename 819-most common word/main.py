class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # pre-process
        PUNCTUATIONS = "!?',;."
        paragraph = paragraph.lower()
        for punctuation in PUNCTUATIONS:
            paragraph = paragraph.replace(punctuation, ' ')
        words = paragraph.split(' ')

        dicts = dict()
        for word in words:
            if word != '' and word not in banned:
                if word not in dicts:
                    dicts[word] = 0
                dicts[word] += 1
        print(dicts)
        dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)

        # process
        ans = dicts[0][0]
        return ans


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = "a."
banned = []

solution = Solution()
print(solution.mostCommonWord(paragraph, banned))
