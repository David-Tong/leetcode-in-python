class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        plates = defaultdict(int)
        candles = list()
        count = 0
        idx = 0
        while idx < len(s):
            if s[idx] == "*":
                count += 1
            elif s[idx] == "|":
                candles.append(idx)
                plates[idx] = count
            idx += 1
        C = len(candles)
        # print(plates)
        # print(candles)

        # process
        from bisect import bisect_left, bisect_right
        ans = list()
        for query in queries:
            left, right = query
            # print(left, right)
            idx_left = bisect_right(candles, left)
            if idx_left > 0:
                if candles[idx_left - 1] == left:
                    idx_left -= 1
            if idx_left == len(candles):
                idx_left -= 1

            idx_right = bisect_left(candles, right)
            if idx_right < len(candles):
                if idx_right > 0 and candles[idx_right] > right:
                    idx_right -= 1
            if idx_right == len(candles):
                idx_right -= 1

            print(idx_left, idx_right)
            if 0 <= idx_left < C  and 0 <= idx_right < C:
                res = plates[candles[idx_right]] - plates[candles[idx_left]]
            else:
                res = 0
            ans.append(max(0, res))
        return ans


s = "**|**|***|"
queries = [[2,5],[5,9]]

s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]


s = "**|**|***|***"
queries = [[1,4],[8,12],[0,1],[10,12]]

s = "***"
queries = [[2,2]]

solution = Solution()
print(solution.platesBetweenCandles(s, queries))
