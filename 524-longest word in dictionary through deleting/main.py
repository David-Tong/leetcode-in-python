class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        # pre-process
        L = len(s)
        words = sorted(dictionary, key=lambda x:(-1 * len(x), x))
        print(words)

        # process
        for word in words:
            idx, idx2 = 0, 0
            while idx < L and idx2 < len(word):
                if s[idx] == word[idx2]:
                    idx2 += 1
                idx += 1
            if idx2 == len(word):
                return word
        return ""


s = "abpcplea"
dictionary = ["ale","apple","monkey","plea","applb"]

s = "abpcplea"
dictionary = ["a","b","c"]

import random, string

def getWord():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10 ** 3))

s = getWord()
print(s)
dictionary = [getWord() for _ in range(10 ** 3)]
print(dictionary)

solution = Solution()
print(solution.findLongestWord(s, dictionary))
