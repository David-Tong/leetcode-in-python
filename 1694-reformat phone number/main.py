class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # pre-process
        number = number.replace(' ', '')
        number = number.replace('-', '')
        L = len(number)

        # process
        idx = 0
        ans = list()
        while L - idx > 4:
            ans.append(number[idx: idx + 3])
            idx += 3

        if L - idx == 4:
            ans.append(number[idx: idx + 2])
            ans.append(number[idx + 2:])
        else:
            ans.append(number[idx:])
        return "-".join(ans)


number = "1-23-45 6"
number = "123 4-567"
number = "123 4-5678"
number = "1-1-2-3"
number = "1-1"
number = "1-1-2"
number = "1-1-2-35"

solution = Solution()
print(solution.reformatNumber(number))
