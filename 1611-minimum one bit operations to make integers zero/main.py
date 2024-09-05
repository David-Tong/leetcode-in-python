class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        zero = defaultdict(int)
        onezeros = defaultdict(int)

        # 101011 => 000000
        # 1(01011) => 1(10000) => 0(10000) => 0(00000)
        # 1(xxxxx) => 1(10000) => 0(10000) => 0(00000)
        # makeZero(1xxxxx) = makeOneZeros(xxxxx) + 1 + makeZero(10000)

        # operations needed to convert any number to 0
        def makeZero(n):
            if n == "0":
                return 0
            if n == "1":
                return 1
            if n in zero:
                return zero[n]
            if n[0] == "0":
                return makeZero(n[1:])
            m = n[1:]
            p = "1" + "0" * (len(n) - 2)
            zero[n] = makeOneZeros(m) + 1 + makeZero(p)
            return zero[n]

        # makeOneZeros(xxxxx)
        # 1xxxx = makeZero(xxxx)
        # 0(xxxx) -> 0(1000) -> 1(1000) -> 1(0000)
        # 0xxxx = makeOneZeros(xxxx) + 1 + makeZero(1000)

        # operations needed to convert any number to 10000
        def makeOneZeros(n):
            if n == "0":
                return 1
            if n == "1":
                return 0
            if n in onezeros:
                return onezeros[n]
            if n[0] == "1":
                onezeros[n] = makeZero(n[1:])
            else:
                m = n[1:]
                p = "1" + "0" * (len(n) - 2)
                onezeros[n] = makeOneZeros(m) + 1 + makeZero(p)
            return onezeros[n]

        return makeZero(bin(n)[2:])


n = 3
n = 6
n = 11
n = 2000
n = 100000000

solution = Solution()
print(solution.minimumOneBitOperations(n))
