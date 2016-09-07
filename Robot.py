all_customers = [22, 32, 52]
print (all_customers[0])
print (all_customers[1])
print (all_customers[2])


customers_by_name = { "bob": "45", "anne": "25"}
print (customers_by_name["bob"])
print (customers_by_name["anne"])

class Product: 
	price = 0
	count = 0
	tax = 1

robot = Product()
robot.price = 900
robot.count = 2
robot.tax = 1.25

book = Product()
book.price = 100 
book.tax = 1.06

print(robot.price * robot.count * robot.tax + book.price * book.tax)






