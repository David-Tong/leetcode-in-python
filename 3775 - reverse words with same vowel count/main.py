class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        VOWELS = 'aeiou'
        words = s.split()
        L = len(words)

        # helper function
        def countVowels(word):
            count = 0
            for ch in word:
                if ch in VOWELS:
                    count += 1
            return count

        # process
        target = countVowels(words[0])
        processed = list()
        processed.append(words[0])
        for x in range(1, L):
            if countVowels(words[x]) == target:
                processed.append(words[x][::-1])
            else:
                processed.append(words[x])
        ans = " ".join(processed)
        return ans


s = "cat and mice"
s = "book is nice"
s = "banana healthy"

solution = Solution()
print(solution.reverseWords(s))
