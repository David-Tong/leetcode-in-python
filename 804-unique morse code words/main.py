class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dicts = dict()
        for word in words:
            code = ""
            for ch in word:
                code = code + morses[ord(ch) - ord('a')]
            if code not in dicts:
                dicts[code] = True
        return len(dicts)


words = ["gin","zen","gig","msg"]
words = ["a"]
words = []

solution = Solution()
print(solution.uniqueMorseRepresentations(words))