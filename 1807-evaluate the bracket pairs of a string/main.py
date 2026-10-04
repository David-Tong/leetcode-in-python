class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        # pre-process
        L = len(s)
        dicts = {key : value for key, value in knowledge}
        print(dicts)

        # process
        ans = ""
        idx = 0
        start = -1
        while idx < L:
            if s[idx] == "(":
                start = idx
            elif s[idx] == ")":
                label = s[start + 1:idx]
                if label in dicts:
                    ans += dicts[label]
                else:
                    ans += "?"
                start = -1
            if start == -1 and s[idx] != ")":
                ans += s[idx]
            idx += 1
        return ans


s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]

s = "hi(name)"
knowledge = [["a","b"]]

solution = Solution()
print(solution.evaluate(s, knowledge))
