# Задание 1_1
На вход поступает двузначное число. Необходимо вывести количество десятков и единиц в нём в формате "Количество десятков: {} Количество единиц: {}"
# Листинг 1_1
```Py
def main():
    number = input()
    print("Количество десятков:", int(number) // 10, "Количество единиц:", int(number) % 10)


if __name__ == "__main__":
    main()
```
________
# Задание 1_2
На вход поступает двузначное число. Необходимо вывести сумму его цифр в формате "Сумма цифр: {}"
# Листинг 1_2
```Py
def main():
    number = input()
    print("Сумма цифр:", int(number) // 10 + int(number) % 10)


if __name__ == "__main__":
    main()
```
________
# Задание 1_3
На вход поступает двузначное число. Необходимо вывести его, поменяв местами десятки и единицы.
# Листинг 1_3
```Py
def main():
    number = input()
    print(int(number) // 10 + int(number) % 10 * 10)


if __name__ == "__main__":
    main()
```
________
# Задание 1_4
На вход подаётся трёхзначное число. Необходимо вывести его цифры через запятую в порядке: сотни, десятки, единицы.
# Листинг 1_4
```Py
def main():
    number = int(input())
    print(str(number // 100) + ", " + str((number - (number // 100 * 100) - (number % 10)) // 10) + ", " + str(number % 10))


if __name__ == "__main__":
    main()
```
________