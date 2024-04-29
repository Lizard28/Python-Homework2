numbersCount = input("Количество чисел: ") # 5

try:
    numbersCount = int(numbersCount)

    if numbersCount <= 0:
        raise ValueError
except ValueError:
    print("Неправильное значение")
    exit(0)

numbersList = [] # ['1.5', '2', 'Ab', '-1', '-3,5']
powersList  = [] # [2, -4, 3, -2, 2]

print("Введите числа или строку по одному:")
for i in range(numbersCount):
    numbersList.append(input())

print("Введите целые степени по одному:")
for i in range(numbersCount):
    powersList.append(int(input()))

for i in range(numbersCount):
    value = numbersList[i]
    power = powersList[i]

    try:
        print(int(value) ** power)
    except ValueError:
        try:
            print(float(value.replace(",", ".")) ** power)
        except ValueError:
            print(value * power)
