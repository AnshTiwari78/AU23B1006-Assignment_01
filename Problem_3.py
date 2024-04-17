def process_order(orders):
    order_stack = []
    for order in orders:
        print("Preparing Your Order -", order)
        order_stack.append(order)
    print("Dispatched order is-")
    while order_stack:
        print(order_stack.pop())
num_orders = int(input("How many orders-"))
orders = []
for i in range(num_orders):
    order = input("Order-")
    orders.append(order)
process_order(orders)