class Product: 
	price = 0
	count = 0
	tax = 0

	def price_with_tax(self):
		return self.price * self.count * self.tax

	def price_with_tax(self):
		total = self.price * self.count * self.tax 
		if total > 500:
			return 0.9 * total 
		else:
			return total

	def __init__(self, price, count, tax):
		self.price = price 
		self.count = count
		self.tax = tax 

products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06), Product(price=1500, count=1, tax=1.25)]
total_price = 0
for product in products:
	total_price += product.price_with_tax()

if total_price > 500:
 	total_price = 0.8 * total_price

print(total_price)





















