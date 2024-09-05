class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for pair in pairs:
            dicts[pair[0]] = pair[1]
            dicts[pair[1]] = pair[0]

        prefs = defaultdict(dict)
        for idx, preference in enumerate(preferences):
            for idx2, prefer in enumerate(preference):
                prefs[idx][prefer] = idx2

        # process
        unhappy = set()
        for x in range(n):
            for y in range(x + 1, n):
                x_pair = dicts[x]
                y_pair = dicts[y]
                if x_pair != y and x != y_pair:
                    if prefs[x][y] < prefs[x][x_pair]:
                        if prefs[y][x] < prefs[y][y_pair]:
                            unhappy.add(x)
                            unhappy.add(y)
        ans = len(unhappy)
        return ans


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

n = 2
preferences = [[1], [0]]
pairs = [[1, 0]]

n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]

solution = Solution()
print(solution.unhappyFriends(n, preferences, pairs))
