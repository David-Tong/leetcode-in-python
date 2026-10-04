class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00

        ans = [kelvin, fahrenheit]
        return ans


celsius = 36.50
celsius = 122.11

solution = Solution()
print(solution.convertTemperature(celsius))
