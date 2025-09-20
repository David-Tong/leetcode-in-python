class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        SEPARATIONS = ['+', '-', '(', ')', ' ']

        # helper function
        # markEmail
        def maskEmail(s):
            s = s.lower()
            name, domain = s.split('@')
            name = name[0] + '*' * 5 + name[-1]
            return "{}@{}".format(name, domain)

        # maskPhone
        def maskPhone(s):
            for separation in SEPARATIONS:
                s = s.replace(separation, '')
            if len(s) == 10:
                return "***-***-{}".format(s[-4:])
            elif len(s) == 11:
                return "+*-***-***-{}".format(s[-4:])
            elif len(s) == 12:
                return "+**-***-***-{}".format(s[-4:])
            elif len(s) == 13:
                return "+***-***-***-{}".format(s[-4:])

        if '@' in s:
            return maskEmail(s)
        else:
            return maskPhone(s)


s = "LeetCode@LeetCode.com"
s = "AB@qq.com"
s = "1(234)567-890"

solution = Solution()
print(solution.maskPII(s))
