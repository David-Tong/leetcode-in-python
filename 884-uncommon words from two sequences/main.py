class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # pre-process
        from collections import defaultdict
        dicts1 = defaultdict(int)
        dicts2 = defaultdict(int)

        for word in s1.split():
            dicts1[word] += 1
        for word in s2.split():
            dicts2[word] += 1

        # process
        uncommons = (set(dicts1.keys()) | set(dicts2.keys())) - (set(dicts1.keys()) & set(dicts2.keys()))
        ans = list()
        for key in uncommons:
            if key in dicts1 and dicts1[key] == 1:
                ans.append(key)
            if key in dicts2 and dicts2[key] == 1:
                ans.append(key)
        return ans


s1 = "this apple is sweet"
s2 = "this apple is sour"

s1 = "apple apple"
s2 = "banana"

s1 = "s z z z s"
s2 = "s z ejt"

solution = Solution()
print(solution.uncommonFromSentences(s1, s2))
