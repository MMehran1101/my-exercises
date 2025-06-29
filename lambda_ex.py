orders = [
    {"item": "Laptop", "price": 1200},
    {"item": "Mouse", "price": 20},
    {"item": "Keyboard", "price": 70},
    {"item": "Monitor", "price": 300}
]
print(orders)

sorted_orders = sorted(orders, key=lambda order: order["price"], reverse=True)

print(sorted_orders)

print("***             End             ***")

users = [
    {"name": "Ali", "is_active": True},
    {"name": "Sara", "is_active": False},
    {"name": "Reza", "is_active": True},
    {"name": "Mina", "is_active": False}
]

active_users = filter(lambda user: user["is_active"], users)
active_users_list = list(active_users)
print(active_users_list)

print("***             End             ***")

names = ["Ali", "Sara", "Reza", "Mina"]

say_hello = list(map(lambda name: "Hello " + name, names))
print(say_hello)

