def fact(number):
    if number == 1:
        return number
    return number*fact(number-1)

number = 5
print(fact(number))