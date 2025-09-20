class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # pre-process
        L = len(word)
        VOWELS = "AEIOUaeiou"

        # process
        # condition 1 - It contains a minimum of 3 characters.
        if L < 3:
            return False

        # condition 2 - It contains only digits (0-9), and English letters (uppercase and lowercase).
        if not word.isalnum():
            return False

        vowel, consonant = 0, 0
        for ch in word:
            if ch.isalpha():
                if ch in VOWELS:
                    vowel += 1
                else:
                    consonant += 1

        # condition 3 - It includes at least one vowel.
        # condition 4 - It includes at least one consonant.
        if vowel == 0 or consonant == 0:
            return False

        return True


word = "234Adas"
word = "b3"
word = "a3$e"
word = "AhI"

solution = Solution()
print(solution.isValid(word))
