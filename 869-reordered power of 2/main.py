class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        LIMIT = 10 ** 9

        from collections import defaultdict
        powers = defaultdict(list)

        # create table
        x = 0
        while True:
            power = pow(2, x)
            if power > LIMIT:
                break
            power = str(power)
            L = len(power)
            dicts = defaultdict(int)
            for ch in power:
                dicts[ch] += 1
            powers[L].append(dicts)
            x += 1

        # lookup table
        n = str(n)
        N = len(n)
        target = defaultdict(int)
        for ch in n:
            target[ch] += 1

        for dicts in powers[N]:
            if len(dicts) == len(target):
                match = True
                for ch in target:
                    if target[ch] == dicts[ch]:
                        pass
                    else:
                        match = False
                        break
                if match:
                    return True
        return False


n = 1
n = 3
n = 1240
n = 991398283
n = 0

solution = Solution()
print(solution.reorderedPowerOf2(n))
