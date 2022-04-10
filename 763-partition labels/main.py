class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        from collections import defaultdict
        dict = defaultdict(list)

        for idx, ch in enumerate(s):
            if ch not in dict:
                dict[ch].append(idx)
                dict[ch].append(idx)
            dict[ch][1] = idx

        intervals = sorted(dict.values(), key=lambda x: (x[0]))
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                ans.append(end - start + 1)
                start = interval[0]
                end = interval[1]
        ans.append(len(s) - start)
        return ans


s = "ababcbacadefegdehijhklij"
s = "eccbbbbdec"
s = "z"
s = "ababcbacadefegdehijhklijz"
s = "ababcbacadefegdehijhklijza"

solution = Solution()
print(solution.partitionLabels(s))