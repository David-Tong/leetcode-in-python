class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = set()
        candidates.add(1224444)
        sequences = [[1],
                     [2, 2], [1, 2, 2], [3, 3, 3],
                     [1, 3, 3, 3], [4, 4, 4, 4],
                     [2, 2, 3, 3, 3], [1, 4, 4, 4, 4], [5, 5, 5, 5, 5],
                     [1, 5, 5, 5, 5, 5], [1, 2, 2, 3, 3, 3], [2, 2, 4, 4, 4, 4], [6, 6, 6, 6, 6, 6]]

        from itertools import permutations
        for sequence in sequences:
            for permutation in permutations(sequence):
                candidates.add(int("".join([str(_) for _ in permutation])))

        candidates = sorted(candidates)
        print(candidates)
        from bisect import bisect_left
        idx = bisect_left(candidates, n)

        return candidates[idx + 1] if candidates[idx] == n else candidates[idx]


n = 1
n = 1000
n = 3000
n = 9999
n = 99999
n = 999999

solution = Solution()
print(solution.nextBeautifulNumber(n))
