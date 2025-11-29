class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(s)

        # helper function
        def findIndexes(s, t):
            T = len(t)
            idx = 0
            res = list()
            while idx < L:
                if idx == 34:
                    pass
                matched = False
                idx2 = 0
                while idx + idx2 < L and idx2 < T:
                    if s[idx + idx2] != t[idx2]:
                        break
                    idx2 += 1
                if idx2 == T:
                    matched = True
                if matched:
                    res.append(idx)
                idx += 1
            return res

        # process
        idxes = findIndexes(s, a)
        idxes2 = findIndexes(s, b)
        # print(idxes)
        # print(idxes2)

        ans = list()
        for x in idxes:
            for y in idxes2:
                if abs(x - y) <= k:
                    ans.append(x)
                    break
        return ans


s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15

s = "abcd"
a = "a"
b = "a"
k = 4

s = "ababababazzabababb"
a = "aba"
b = "bb"
k = 10

solution = Solution()
print(solution.beautifulIndices(s, a, b, k))
