class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # pre-process
        from collections import Counter
        count = Counter(word)
        # print(count)

        # process
        from collections import defaultdict
        values = defaultdict(int)
        for value in count.values():
            values[value] += 1
        print(values)

        # conner case
        if len(values.keys()) == 1:
            # "bac"
            if values.keys()[0] == 1:
                return True
            # "zz"
            if values.values()[0] == 1:
                return True

        if len(values.keys()) != 2:
            return False
        maxi, mini = max(values), min(values)
        if maxi - mini != 1:
            # corner case
            # "cccd"
            if mini == 1:
                # conner case
                # "cbccca"
                if values[mini] == 1:
                    return True
                else:
                    return False
            else:
                return False
        if values[maxi] == 1:
            return True

        # corner case
        # "abbcc"
        if values[mini] == 1:
            if mini == 1:
                return True
        return False


word = "abcc"
word = "aazz"
word = "aabbbccc"
word = "aaaabb"
"""
word = "abbccc"
word = "bac"
word = "zz"
word = "cccd"
"""

solution = Solution()
print(solution.equalFrequency(word))
