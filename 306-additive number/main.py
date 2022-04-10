class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def checkSum(num, sumi, j):
            for k in range(len(sumi)):
                if k + j >= len(num) or sumi[k] != num[k + j]:
                    return False
            return True

        def doAdd(num):
            if len(num) == 0:
                return True

            N = len(num)
            for i in range(1, N):
                for j in range(i + 1, N):
                    num1 = num[:i]
                    num2 = num[i:j]

                    if len(num1) > 1:
                        if num1[0] == "0":
                            break
                    if len(num2) > 1:
                        if num2[0] == "0":
                            break

                    sumi = str(int(num1) + int(num2))
                    if checkSum(num, sumi, j):
                        if j + len(sumi) == N:
                            return True
                        else:
                            if doAdd(num[len(num1):]):
                                return True
            return False

        return doAdd(num)


num = "112358"
#num = "199100199"
#num = "1023"
num = "12122436"

solution = Solution()
print(solution.isAdditiveNumber(num))
