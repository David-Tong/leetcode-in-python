class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # process
        dicts = set()
        ans = list()

        partition = ""
        for ch in s:
            partition += ch
            if partition not in dicts:
                dicts.add(partition)
                ans.append(partition)
                partition = ""
        return ans


s = "abbccccd"
s = "aaaa"

solution = Solution()
print(solution.partitionString(s))
