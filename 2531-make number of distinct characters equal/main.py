import string


class Solution(object):
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # swap ch1 from counter1 to counter2 and ch2 from counter2 to counter1
        def swapCompare(counter1, counter2, ch1, ch2):
            # swap
            counter1[ch1] -= 1
            if counter1[ch1] == 0:
                del counter1[ch1]
            counter2[ch2] -= 1
            if counter2[ch2] == 0:
                del counter2[ch2]
            counter1[ch2] += 1
            counter2[ch1] += 1

            equal = len(counter1) == len(counter2)

            # swap back
            counter1[ch2] -= 1
            if counter1[ch2] == 0:
                del counter1[ch2]
            counter2[ch1] -= 1
            if counter2[ch1] == 0:
                del counter2[ch1]
            counter1[ch1] += 1
            counter2[ch2] += 1

            return equal

        from collections import Counter
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1
        diff = len(counter2) - len(counter1)

        if diff <= 2:
            for ch1 in counter1:
                for ch2 in counter2:
                    if swapCompare(counter1, counter2, ch1, ch2):
                        return True

        return False


word1 = "ac"
word2 = "b"

word1 = "abcc"
word2 = "aab"

word1 = "abcde"
word2 = "fghij"

word1 = "aaa"
word2 = "abc"

"""
word1 = "a"
word2 = "bb"

word1 = "aaadhg"
word2 = "bgh"

word1 = "ac"
word2 = "caca"

word1 = "fafdd"
word2 = "fbdc"
"""

solution = Solution()
print(solution.isItPossible(word1, word2))
