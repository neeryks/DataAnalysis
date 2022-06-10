summ = 0
for i in range(21):
    if i % 2 != 0  or i % 3 != 0 or i % 5 != 0:
        summ += i
print(summ)