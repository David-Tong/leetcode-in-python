class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = len(word)

        # helper function
        def getOrder(idx, order):
            if word[idx] == "a":
                    return 1
            elif order == 1:
                if word[idx] == "a":
                    return 1
                elif word[idx] == "e":
                    return 2
            elif order == 2:
                if word[idx] == "e":
                    return 2
                elif word[idx] == "i":
                    return 3
            elif order == 3:
                if word[idx] == "i":
                    return 3
                elif word[idx] == "o":
                    return 4
            elif order == 4:
                if word[idx] == "o":
                    return 4
                elif word[idx] == "u":
                    return 5
            elif order == 5:
                if word[idx] == "u":
                    return 5
            return 0

        # process
        left = 0
        right = 0
        ordered = 0
        ans = 0
        while right < L:
            previous_order = ordered
            ordered = getOrder(right, ordered)
            if ordered == 5:
                ans = max(ans, right - left + 1)

            if previous_order != 1 and ordered == 1:
                left = right
            right += 1
        return ans


word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
word = "aeeeiiiioooauuuaeiou"
word = "a"

import random
word = "".join(random.choice("aeiou") for _ in range(5 * 10 ** 5))
print(word)

"""
word = "u"
word = "eiou"
word = "ou"
"""

solution = Solution()
print(solution.longestBeautifulSubstring(word))
