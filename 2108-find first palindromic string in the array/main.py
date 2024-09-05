class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def isPalindrome(word):
            left = 0
            right = len(word) - 1

            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        for word in words:
            if isPalindrome(word):
                return word
        return ""


words = ["abc","car","ada","racecar","cool"]
words = ["notapalindrome","racecar"]
words = ["def","ghi"]
words = ["def","ghi","gg"]
words = ["a"]

solution = Solution()
print(solution.firstPalindrome(words))
