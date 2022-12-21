from entity.order import Order
from entity.address import Address
from entity.customer import Customer
from entity.order_item import OrderItem
from service.product_service import ProductService

# Customer Aggregate
customer = Customer("123", "Joao Maria")
address = Address(
    street="street 1",
    number=2,
    zip="123456",
    city="A city")

customer.set_address(address)
customer.activate()

# Order Aggregate
item1 = OrderItem("1", "Item 1", 10.5, "id1", 5)
item2 = OrderItem("2", "Item 2", 20, "id2", 10)

order = Order("1", "123", [item1, item2])
pass
