class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        # pre-process
        if x >= y:
            first, second = "a", "b"
            maxi, mini = x, y
        else:
            first, second = "b", "a"
            maxi, mini = y, x

        # process
        stack = list()
        ans = 0
        for ch in s:
            stack.append(ch)
            if len(stack) > 1:
                if stack[-2] == first and stack[-1] == second:
                    ans += maxi
                    stack.pop()
                    stack.pop()

        s = "".join(stack)
        stack = list()
        for ch in s:
            stack.append(ch)
            if len(stack) > 1:
                if stack[-2] == second and stack[-1] == first:
                    ans += mini
                    stack.pop()
                    stack.pop()
        return ans


s = "cdbcbbaaabab"
x = 4
y = 5

s = "aabbaaxybbaabb"
x = 5
y = 4

s = "aabbabsdbaadbandbwibabasbaabaabdewfwqadb"
x = 6
y = 3

s = "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha"
x = 1926
y = 4320

solution = Solution()
print(solution.maximumGain(s, x, y))
