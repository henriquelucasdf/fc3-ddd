from uuid import uuid4

from src.domain.order.factory.order_factory import OrderFactory


def test_should_create_an_order():
    order_args = {
        "id": str(uuid4()),
        "customer_id": str(uuid4()),
        "items": [
            {
                "id": str(uuid4()),
                "name": "Product 1",
                "product_id": str(uuid4()),
                "quantity": 1,
                "price": 100
            }
        ]
    }

    order = OrderFactory.create(order_args)

    assert order._id == order_args["id"]
    assert order._customerId == order_args["customer_id"]
    assert len(order._items) == 1
