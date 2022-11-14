class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(self.size)]
        self.ranks = [0] * self.size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.ranks[px] > self.ranks[py]:
                self.parents[py] = px
            elif self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
            else:
                self.parents[py] = px
                self.ranks[px] += 1
            return True

    def equal(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        else:
            return False


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        ufs = UnionFindSet(26)

        # check equations, keep inequations
        from collections import defaultdict
        dicts = defaultdict(int)
        inequations = list()
        for idx, equation in enumerate(equations):
            if equation[1] == "!":
                inequations.append(idx)
            elif equation[1] == "=":
                # check equations
                num = ord(equation[0]) - ord('a')
                num2 = ord(equation[3]) - ord('a')
                if num == num2:
                    continue
                ufs.union(num, num2)

        # check inequations
        for idx in inequations:
            num = ord(equations[idx][0]) - ord('a')
            num2 = ord(equations[idx][3]) - ord('a')
            if num == num2:
                return False
            if ufs.equal(num, num2):
                return False

        return True


equations = ["a==b", "b!=a"]
equations = ["b==a", "a==b"]
equations = ["a==b", "b==c", "a!=d"]
equations = ["a==b", "b==c", "a!=c"]
equations = ["a!=b", "b!=c", "a==c"]
equations = ["a!=a"]
equations = ["c==c", "f!=a", "f==b", "b==c"]
equations = ["b==d", "c==a", "h==a", "d==d", "a==b", "h!=k", "i==h"]

solution = Solution()
print(solution.equationsPossible(equations))
