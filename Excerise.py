#       *** Weight Calculator ***


# weight = float(input("Weight: "))
# weigthTransfer = input("K(g) or (L)bs: ")
#
#
# if weigthTransfer in ("k", "K"):
#     weight /= 0.45
#     print("Weight in lbs :", weight)
# elif weigthTransfer in ("l", "L"):
#     weight *= 0.45
#     print("Weight in Kg :", weight)

#                   *** End ***

import inflect

p = inflect.engine()


def OneTo100(fromThis, toThis):
    while fromThis <= toThis:
        print(str(fromThis), p.number_to_words(fromThis))
        fromThis += 1
    return print(str("GOOD WORK!!!").lower())


try:
    number = int(input("Give me a number: "))
    print(f"One divided by {p.number_to_words(number)}({number}) : ", 1 / number)
except ZeroDivisionError:
    print("You are devided zero by zero !!! STUPID !")

except ValueError:
    print("TYPE INTIGER not anything else!!")
finally:
    f = int(input("Count From ?? "))
    t = int(input("To ?? "))
    OneTo100(f, t)
