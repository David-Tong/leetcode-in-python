class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        # pre-process
        L = len(num)
        LIMIT = 2 ** 31

        # process
        def dfs(idx, num1, num2, splits):
            if idx == L:
                if len(splits) >= 3:
                    res = splits
                    return res
            else:
                if num1 == -1:
                    for x in range(1, 11):
                        if x > 1 and num[idx] == '0':
                            continue
                        if idx + x <= L:
                            num1 = int(str(num[idx:idx + x]))
                            if num1 < LIMIT:
                                res = dfs(idx + x, num1, num2, [num1])
                                if res:
                                    return res

                elif num2 == -1:
                    for x in range(1, 11):
                        if x > 1 and num[idx] == '0':
                            continue
                        if idx + x <= L:
                            num2 = int(str(num[idx:idx + x]))
                            if num2 < LIMIT:
                                res = dfs(idx + x, num1, num2, [num1, num2])
                                if res:
                                    return res
                else:
                    for x in range(1, 11):
                        if x > 1 and num[idx] == '0':
                            continue
                        if idx + x <= L:
                            target = int(str(num[idx:idx + x]))
                            if target == num1 + num2:
                                if target < LIMIT:
                                    res = dfs(idx + x, num2, target, splits + [target])
                                    if res:
                                        return res

        ans = dfs(0, -1, -1, list())
        if not ans:
            ans = list()
        return ans


num = "1101111"
num = "112358130"
num = "0123"
num = "1011"
num = "502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310"

solution = Solution()
print(solution.splitIntoFibonacci(num))
