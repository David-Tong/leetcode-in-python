class ProductOfNumbers(object):

    def __init__(self):
        self.nums = list()

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        L = len(self.nums)
        product = 1
        for x in range(L - k, L):
            product *= self.nums[x]
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

pon = ProductOfNumbers()
pon.add(3)
pon.add(0)
pon.add(2)
pon.add(5)
pon.add(4)
print(pon.getProduct(2))
print(pon.getProduct(3))
print(pon.getProduct(4))
pon.add(8)
print(pon.getProduct(2))
