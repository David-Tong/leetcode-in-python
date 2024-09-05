class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        pairs = zip(difficulty, profit)
        pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

        from collections import defaultdict
        book = defaultdict(int)
        maxi = 0
        for pair in pairs:
            maxi = max(maxi, pair[1])
            book[pair[0]] = maxi

        from bisect import bisect_left
        diff = sorted(book.keys())
        L = len(diff)

        ans = 0
        for wrk in worker:
            idx = bisect_left(diff, wrk)
            if idx == 0:
                if wrk == diff[idx]:
                    ans += book[diff[idx]]
            elif idx == L:
                ans += book[diff[idx - 1]]
            else:
                if wrk == diff[idx]:
                    ans += book[diff[idx]]
                else:
                    ans += book[diff[idx - 1]]
        return ans


difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]

difficulty = [2,4,6,8,10]
profit = [30,20,30,40,50]
worker = [4,5,6,7]

difficulty = [13,37,58]
profit = [4,90,96]
worker = [34,73,45]

difficulty = [27,28,31,44,44]
profit = [29,39,60,84,93]
worker = [67,53,61,56,63]

difficulty = [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
profit = [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
worker = [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]

solution = Solution()
print(solution.maxProfitAssignment(difficulty, profit, worker))