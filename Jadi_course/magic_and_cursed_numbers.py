# تمرین طلسم اعداد جادویی

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Legendary !!")
elif n % 3 == 0:
    print("Magical !")
elif n % 5 == 0:
    print("Cursed !!!!")
else:
    print("Just a normal")
