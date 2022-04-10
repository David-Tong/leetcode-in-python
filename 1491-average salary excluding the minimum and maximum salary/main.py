class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        mini = float("inf")
        maxi = float("-inf")
        sumi = 0
        for asalary in salary:
            mini = min(mini, asalary)
            maxi = max(maxi, asalary)
            sumi += asalary

        return (sumi - maxi - mini + 0.0) / (len(salary) - 2)


salary = [4000,3000,1000,2000]
salary = [1000, 2000, 3000]
salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]

solution = Solution()
print(solution.average(salary))
