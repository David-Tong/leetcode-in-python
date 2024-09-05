import string


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)

        # global cache
        cache = dict()

        # (x, y) - the number of insertion to make s[x:y + 1] a palindrome
        def doInsert(x, y):
            key = str(x) + "-" + str(y)
            if key in cache:
                return cache[key]

            if x >= y:
                return 0

            if s[x] == s[y]:
                inserts = min(doInsert(x + 1, y - 1), min(doInsert(x + 1, y), doInsert(x, y - 1)) + 1)
            else:
                inserts = min(doInsert(x + 1, y), doInsert(x, y - 1)) + 1

            cache[key] = inserts
            return inserts

        return doInsert(0, L - 1)


s = "zzazz"
s = "abba"
s = "mbadm"
s = "leetcode"
s = "abasjfhjkkljanr"
s = "abaab"

solution = Solution()
print(solution.minInsertions(s))
