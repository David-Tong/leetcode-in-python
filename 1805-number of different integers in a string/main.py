class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = len(word)

        # process
        start = -1
        s = set()
        idx = 0
        while idx < L:
            if word[idx].isnumeric():
                if start == -1:
                    start = idx
            else:
                if start != -1:
                    num = word[start:idx]
                    num = int(num)
                    s.add(num)
                    start = -1
            idx += 1

        num = word[start:idx]
        if num.isnumeric():
            num = int(num)
            s.add(num)

        ans = len(s)
        return ans


word = "a123bc34d8ef34"
word = "leet1234code234"
word = "a1b01c001"

solution = Solution()
print(solution.numDifferentIntegers(word))
