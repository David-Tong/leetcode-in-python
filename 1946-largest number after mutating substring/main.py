class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        # pre-process
        L = len(num)

        # help function
        def doChange(idx):
            n = int(num[idx])
            if n < change[n]:
                return 1
            elif n > change[n]:
                return -1
            else:
                return 0

        idx = 0
        start = -1
        end = L
        while idx < L:
            if start < 0:
                if doChange(idx) > 0:
                    start = idx
            if start >= 0:
                if doChange(idx) < 0:
                    end = idx
                    break
            idx += 1

        # process
        if start == -1:
            return num
        ans = num[:start]
        idx = start
        while idx < end:
            ans += str(change[int(num[idx])])
            idx += 1
        ans += num[end:]
        return ans


num = "132"
change = [9,8,5,0,3,6,4,2,6,8]

num = "021"
change = [9,4,3,5,7,2,1,9,0,6]

num = "5"
change = [1,4,7,5,3,2,5,6,9,4]

num = "123"
change = [1,2,3,4,5,6,7,8,9,0]

num = "123"
change = [9,0,1,2,3,4,5,6,7,8]

num = "334111"
change = [0,9,2,3,3,2,5,5,5,5]

num = "214010"
change = [6,7,9,7,4,0,3,4,4,7]

solution = Solution()
print(solution.maximumNumber(num, change))
