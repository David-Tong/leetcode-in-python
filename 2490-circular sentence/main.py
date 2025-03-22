class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if sentence[0] != sentence[-1]:
            return False

        L = len(sentence)
        for x in range(L):
            if sentence[x] == " ":
                if sentence[x - 1] != sentence[x + 1]:
                    return False

        return True


sentence = "leetcode exercises sound delightful"
sentence = "eetcode"
sentence = "Leetcode is cool"

solution = Solution()
print(solution.isCircularSentence(sentence))
