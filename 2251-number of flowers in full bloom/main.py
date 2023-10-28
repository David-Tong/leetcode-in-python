class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        blooms = defaultdict(int)
        for flower in flowers:
            blooms[flower[0]] += 1
            blooms[flower[1] + 1] -= 1

        totals = defaultdict(int)
        totals[0] = 0
        prev_key = 0
        for key in sorted(blooms.keys()):
            totals[key] = totals[prev_key] + blooms[key]
            prev_key = key

        # binary search
        from bisect import bisect_left
        keys = sorted(totals.keys())
        ans = list()
        for ppl in people:
            idx = bisect_left(keys, ppl)
            if idx >= len(keys):
                ans.append(0)
            else:
                if keys[idx] == ppl:
                    ans.append(totals[keys[idx]])
                else:
                    ans.append(totals[keys[idx - 1]])
        return ans


flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]

flowers = [[1,10],[3,3]]
people = [3,3,2]

flowers = [[2,8],[5,6],[5,8],[6,11],[2,15]]
people = [1,3,7,8,9,16,19]

flowers = [[2,8]]
people = [1]

flowers = [[11,11],[24,46],[3,25],[44,46]]
people = [1,8,26,7,43,26,1]

solution = Solution()
print(solution.fullBloomFlowers(flowers, people))
