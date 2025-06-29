i = int(input("enter price of your shopping : "))


def discount(value, dis):
    d = value * (dis / 100)
    return int(value - d)


if i > 50000:
    print(f"You will receive a 20% discount.\n"
          f"Total amount: {i}\n"
          f"You pay :", discount(i, 20))
elif i >= 20000 and i <= 50000:
    print(f"You will receive a 10% discount.\n"
          f"Total amount: {i}\n"
          f"You pay :", discount(i, 10))
elif i < 20000:
    print("No Discount, You pay :", i)
