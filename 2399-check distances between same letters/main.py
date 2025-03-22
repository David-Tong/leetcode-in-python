class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, ch in enumerate(s):
            dicts[ch].append(idx)

        # process
        for ch in dicts:
            idx = ord(ch) - ord('a')
            if distance[idx] != dicts[ch][1] - dicts[ch][0] - 1:
                return False
        return True


s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

s = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

solution = Solution()
print(solution.checkDistances(s, distance))
