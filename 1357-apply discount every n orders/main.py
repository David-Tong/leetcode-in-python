class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        from collections import defaultdict
        self.prices = defaultdict(int)
        idx = 0
        while idx < len(products):
            self.prices[products[idx]] = prices[idx]
            idx += 1
        self.count = 0

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        res = 0
        idx = 0
        while idx < len(product):
            res += self.prices[product[idx]] * amount[idx]
            idx += 1

        self.count += 1
        if self.count % self.n == 0:
            res = res * (100 - self.discount) * 1.0 / 100
        return res

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
n = 3
discount = 50
products = [1,2,3,4,5,6,7]
prices = [100,200,300,400,300,200,100]
cashier = Cashier(n, discount, products, prices)

product = [1,2]
amount = [1,2]
print(cashier.getBill(product, amount))

product = [3,7]
amount = [10,10]
print(cashier.getBill(product, amount))

product = [1,2,3,4,5,6,7]
amount = [1,1,1,1,1,1,1]
print(cashier.getBill(product, amount))

product = [4]
amount = [10]
print(cashier.getBill(product, amount))

product = [7,3]
amount = [10,10]
print(cashier.getBill(product, amount))

product = [7,5,3,1,6,4,2]
amount = [10,10,10,9,9,9,7]
print(cashier.getBill(product, amount))

product = [2,3,5]
amount = [5,3,2]
print(cashier.getBill(product, amount))
