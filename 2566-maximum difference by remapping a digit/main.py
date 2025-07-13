class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        # pre-process
        num = str(num)
        L = len(num)

        # process
        # find maxi
        remapping = ''
        for x in range(L):
            if num[x] != '9':
                remapping = num[x]
                break
        maxi = ""
        for x in range(L):
            if num[x] == remapping:
                maxi += "9"
            else:
                maxi += num[x]
        maxi = int(maxi)

        # find mini
        remapping = ''
        for x in range(L):
            if num[x] != '0':
                remapping = num[x]
                break
        mini = ""
        for x in range(L):
            if num[x] == remapping:
                mini += "0"
            else:
                mini += num[x]
        mini = int(mini)

        # post-process
        ans = maxi - mini
        return ans


num = 11891
num = 90
num = 99999
num = 0
num = 10000000

solution = Solution()
print(solution.minMaxDifference(num))
