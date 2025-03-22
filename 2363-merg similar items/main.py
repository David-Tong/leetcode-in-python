class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        for value, weight in items1:
            dicts[value] += weight
        for value, weight in items2:
            dicts[value] += weight

        # post-process
        ans = list()
        for key in sorted(dicts.keys()):
            ans.append((key, dicts[key]))
        return ans


items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]

items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]

items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]

solution = Solution()
print(solution.mergeSimilarItems(items1, items2))
