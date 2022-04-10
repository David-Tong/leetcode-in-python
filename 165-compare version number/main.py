class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def parseVersion(version):
            reversions = version.split(".")
            vers = list()
            for reversion in reversions:
                index = 0
                while index < len(reversion) and reversion[index] == "0":
                    index += 1
                if index < len(reversion):
                    vers.append(reversion[index:])
                else:
                    vers.append('0')
            return vers

        vers1 = parseVersion(version1)
        vers2 = parseVersion(version2)

        index1 = 0
        index2 = 0
        while index1 < len(vers1) and index2 < len(vers2):
            if int(vers1[index1]) < int(vers2[index2]):
                return -1
            elif int(vers1[index1]) > int(vers2[index2]):
                return 1
            else:
                index1 += 1
                index2 += 1

        while index1 < len(vers1):
            if vers1[index1] != '0':
                return 1
            index1 += 1

        while index2 < len(vers2):
            if vers2[index2] != '0':
                return -1
            index2 += 1

        return 0


version1 = "1.01"
version2 = "1.001"

version1 = "1.0"
version2 = "1.0.0"

version1 = "0.1"
version2 = "1.1"

version1 = "000.01.00"
version2 = "000.01.01"

version1 = "1.0"
version2 = "1.0.0"

version1 = "1.2"
version2 = "1.10"

solution = Solution()
print(solution.compareVersion(version1, version2))
