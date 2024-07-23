class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defangs = address.split(".")
        return "[.]".join(defangs)


address = "1.1.1.1"
address = "255.100.50.0"

solution = Solution()
print(solution.defangIPaddr(address))
