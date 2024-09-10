class UnionFindSet(object):
    def __init__(self):
        self.N = 26
        self.parents = [x for x in range(self.N)]
        self.ranks = [0] * self.N

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True


class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        ufs = UnionFindSet()

        L = len(s1)
        for x in range(L):
            ufs.union(ord(s1[x]) - ord('a'), ord(s2[x]) - ord('a'))

        for x in range(26):
            ufs.find(x)

        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, parent in enumerate(ufs.parents):
            dicts[parent].append(idx)

        maps = defaultdict(chr)
        for key, value in dicts.items():
            for item in value:
                maps[chr(ord('a') + item)] = chr(ord('a') + value[0])

        ans = ""
        for ch in baseStr:
            ans += maps[ch]
        return ans


s1 = "abc"
s2 = "cde"
baseStr = "eed"

s1 = "parker"
s2 = "morris"
baseStr = "parser"

s1 = "hello"
s2 = "world"
baseStr = "hold"

s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"

solution = Solution()
print(solution.smallestEquivalentString(s1, s2, baseStr))
