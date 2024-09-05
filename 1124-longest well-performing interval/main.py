class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        # pre-process
        L = len(hours)

        wpis = [0]
        for hour in hours:
            if hour > 8:
                wpis.append(wpis[-1] + 1)
            else:
                wpis.append(wpis[-1] - 1)
        print(wpis)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        ans = 0
        for idx, wpi in enumerate(wpis):
            target = min(0, wpi - 1)
            if target in dicts:
                ans = max(ans, idx - dicts[target])
            if wpi not in dicts:
                dicts[wpi] = idx
        return ans


hours = [9,9,6,0,6,6,9]
hours = [6,6,6]
hours = [5,4,9,9,9,9,9,11,0,2,3,4]
hours = [9,6,9]
hours = [10,8,8,12,6,6,7,11,11,9,11]
hours = [9,9,9]

solution = Solution()
print(solution.longestWPI(hours))
