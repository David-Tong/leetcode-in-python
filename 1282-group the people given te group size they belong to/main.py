class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        dicts = defaultdict(list)
        counters = defaultdict(int)

        ans = list()
        for idx, groupSize in enumerate(groupSizes):
            dicts[groupSize].append(idx)
            counters[groupSize] += 1
            if counters[groupSize] % groupSize == 0:
                ans.append(dicts[groupSize])
                dicts[groupSize] = list()
        return ans


groupSizes = [3,3,3,3,3,1,3]
groupSizes = [2,1,3,3,3,2]
groupSizes = [6,6,6,6,6,6]
groupSizes = [1,1,1,1,1,1]
groupSizes = [1]

solution = Solution()
print(solution.groupThePeople(groupSizes))
