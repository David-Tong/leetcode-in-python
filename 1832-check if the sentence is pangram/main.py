class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dicts = {}
        count = 0
        for ch in sentence:
            if not ch in dicts:
                dicts[ch] = True
                count += 1
            if count == 26:
                return True
        return False


sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"

solution = Solution()
print(solution.checkIfPangram(sentence))
