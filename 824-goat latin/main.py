class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        # process
        VOWELS = ['a', 'e', 'i', 'o', 'u']

        words = sentence.split()
        converted = list()
        for idx, word in enumerate(words):
            if word[0].lower() in VOWELS:
                converted.append(word + 'ma' + 'a' * (idx + 1))
            else:
                converted.append(word[1:] + word[0] + 'ma' + 'a' * (idx + 1))
        ans = " ".join(converted)
        return ans


sentence = "I speak Goat Latin"
sentence = "The quick brown fox jumped over the lazy dog"

solution = Solution()
print(solution.toGoatLatin(sentence))
