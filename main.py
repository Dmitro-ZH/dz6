#завдання 2

while True:
    try:
        number = round(float(input("введіть число ")))
    except (ValueError):
        print("ви уввели неправильне число")
    else:
        print(number)
        break