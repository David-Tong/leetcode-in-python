class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def doDecode(s):
            if "[" not in s and "]" not in s:
                return s
            stack = []
            index = 0
            start = 0
            ans = ""
            number = ""
            while index < len(s):
                if s[index] == "[":
                    if len(stack) == 0:
                        start = index
                    stack.append(number)
                    number = ""
                elif s[index] == "]":
                    if len(stack) == 1:
                        ans += int(stack.pop()) * doDecode(s[start+1:index])
                    else:
                        stack.pop()
                elif s[index].isdigit():
                    number += s[index]
                else:
                    if len(stack) == 0:
                        ans += s[index]
                index += 1
            return ans

        return doDecode(s)


s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
s = "3[a2[c]b]"
s = "12[a2[c]b1[d]ef]"

solution = Solution()
print(solution.decodeString(s))
