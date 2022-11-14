class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def getLength(octet):
            if octet[0] == "0":
                return 0
            elif octet[:3] == "110":
                return 1
            elif octet[:4] == "1110":
                return 2
            elif octet[:5] == "11110":
                return 3
            else:
                return -1

        def checkSignificance(octet):
            return octet[:2] == "10"

        L = len(data)
        octets = [bin(datum)[2:].zfill(8) for datum in data]

        #print(octets)

        x = 0
        while x < L:
            octet = octets[x]
            length = getLength(octet)
            if length == -1:
                return False
            if x + length >= L:
                return False
            y = 1
            while y <= length:
                if not checkSignificance(octets[x + y]):
                    return False
                y += 1
            x += y

        return True


data = [197,130,1]
data = [235,140,4]
data = [237]
data = [1]

solution = Solution()
print(solution.validUtf8(data))
