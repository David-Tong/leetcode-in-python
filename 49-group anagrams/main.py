class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        N = len(strs)
        if N == 0:
            return []

        from collections import defaultdict
        map = defaultdict(str)
        for i in range(N):
            key = ''.join(sorted(strs[i]))
            if key in map.keys():
                map[key].append(i)
            else:
                map[key] = [i]

        res = []
        for key in map.keys():
            res.append([strs[k] for k in map[key]])

        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

solution = Solution()
print(solution.groupAnagrams(strs))