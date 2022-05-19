class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        from math import ceil
        repeat = int(ceil(len(b) // len(a)) + 2)

        for x in range(repeat):
            s = a * (x + 1)
            if s.find(b) != -1:
                return x + 1
        return -1


a = "abcd"
b = "cdabcdab"

#a = "a"
#b = "aa"

#a = "abcd"
#b ="cdabcdabcd"

#a = "abc"
#b = "cabcac"

#a = "abc"
#b = "cabcabcabca"

#a = "aaac"
#b = "aac"

#a = "aa"
#b = "a"

#a = "aa"
#b = "aa"

#a = "aaaaaaaaaaaaaaaaaaaaaab"
#b = "ba"

#a = "abcd"
#b = "abcdb"

#a = "aaac"
#b = "aac"

#a = "abcd"
#b = "bcdab"

#a = "abcabcabcabc"
#b = "abac"

solution = Solution()
print(solution.repeatedStringMatch(a, b))
