class UnionFindSet(object):

    def __init__(self, N):
        self.size = N
        self.parents = [_ for _ in range(N)]
        self.ranks = [0] * N

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return False
        else:
            if self.ranks[parent_x] > self.ranks[parent_y]:
                self.parents[parent_y] = parent_x
            elif self.ranks[parent_x] < self.ranks[parent_y]:
                self.parents[parent_x] = parent_y
            else:
                self.parents[parent_y] = parent_x
                self.ranks[parent_x] += 1
            return True


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        ufs = UnionFindSet(len(accounts))

        from collections import defaultdict
        emails = defaultdict(list)

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emails:
                    emails[email] = list()
                emails[email].append(idx)

        for email in emails:
            idx = emails[email][0]
            for idx2 in emails[email][1:]:
                ufs.union(idx, idx2)

        dicts = defaultdict(list)
        for idx, account in enumerate(accounts):
            ufs.find(idx)
            key = ufs.parents[idx]
            if key not in dicts:
                dicts[key].append(account[0])
                dicts[key].append(set())
            for email in account[1:]:
                dicts[key][1].add(email)

        ans = []
        for key in dicts:
            ans.append([dicts[key][0]] + sorted(dicts[key][1]))
        return ans


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

accounts = [["David","David0@m.co","David0@m.co","David1@m.co"],
            ["David","David6@m.co","David1@m.co","David6@m.co"],
            ["David","David3@m.co","David8@m.co","David0@m.co"],
            ["David","David5@m.co","David8@m.co","David7@m.co"],
            ["David","David5@m.co","David2@m.co","David1@m.co"],
            ["David","David0@m.co","David7@m.co","David6@m.co"],
            ["David","David0@m.co","David1@m.co","David4@m.co"],
            ["David","David1@m.co","David1@m.co","David8@m.co"]]
"""
accounts = [["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]]
"""
solution = Solution()
print(solution.accountsMerge(accounts))
