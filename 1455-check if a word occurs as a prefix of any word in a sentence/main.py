class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        # pre-process
        words = sentence.split()
        L = len(searchWord)

        # process
        for idx, word in enumerate(words):
            if len(word) >= L:
                if word[:L] == searchWord:
                    return idx + 1
        return -1


sentence = "i love eating burger"
searchWord = "burg"

sentence = "this problem is an easy problem"
searchWord = "pro"

sentence = "i am tired"
searchWord = "you"

solution = Solution()
print(solution.isPrefixOfWord(sentence, searchWord))
