# logical operators = used on conditional statments
#          and = checks two or more conditions if True
#          or = checks if at least one conditio is True
#          not = Trur if condition is False, and vice versa


temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperatureis good")

if not sunny:
    print("IT is cloudy outside")
else:
    print("It is sunny outside")