class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        # pre-process
        devices = list()
        for bnk in bank:
            device = 0
            for dvc in bnk:
                if dvc == "1":
                    device += 1
            if device > 0:
                devices.append(device)

        # process
        L = len(devices)
        ans = 0
        for x in range(L - 1):
            ans += devices[x] * devices[x + 1]
        return ans


bank = ["011001","000000","010100","001000"]
bank = ["000","111","000"]
bank = ["1111000","0000000","1100111","1111000","0010010"]

solution = Solution()
print(solution.numberOfBeams(bank))
