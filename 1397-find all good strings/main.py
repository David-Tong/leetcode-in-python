class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        # pre-process
        # helper function
        # count - count the number of string alphabetically smaller than or equal to s
        #         and doesn't contain the string evil
        def count(s, evil):
            L = len(s)
            if L == 0:
                return 0

            number = (ord(s[0]) - ord('a')) * 26 ** (L - 1)
            number2 = count(s[1:])
            return number + number2


        print(count(s1))
        print(count(s2))

        return count(s2) - count(s1) + 1


n = 2
s1 = "aa"
s2 = "da"
evil = "b"

solution = Solution()
print(solution.findGoodStrings(n, s1, s2, evil))
