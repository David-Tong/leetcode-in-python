class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        for item in arr:
            dicts[item] += 1

        reversed_dicts = defaultdict(int)
        for k, v in dicts.items():
            if reversed_dicts[v] >= 1:
                return False
            reversed_dicts[v] += 1
        return True


arr = [1,2,2,1,1,3]
arr = [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]

solution = Solution()
print(solution.uniqueOccurrences(arr))
