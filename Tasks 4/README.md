# Задание 4_1
Проверить, является ли число палиндромом.
# Листинг 4_1
```Py

def main():
    number = input()
    if number == number[::-1]:
        print(True)


if __name__ == "__main__":
    main()
```
________
# Задание 4_2
Развернуть число. При этом если в изначальном числе стоит ноль или два нуля их надо убрать. Если число отрицательное, минус сохраняется. Выходное число должно быть в интервале [-128, 128)
# Листинг 4_2
```Py

```
________
# Задание 4_3
На вход поступает строка и целое значение.
Необходимо вывести строку в зигзагообразном виде, где целое значение обозначает количество строк.
Другими типами данных пользоваться нельзя.
Начинать сверху вниз.

![image](https://user-images.githubusercontent.com/115029692/212713556-81011a01-6e58-433e-9743-2bc5c85d2e74.png)

Input: перфекционист, 3

Output: пеотефкинсрци
# Листинг 4_3
```Py

def main():
    string = input()
    number = int(input())
    output = ""
    differ = (number - 3) * 2 + 4
    start_inds = list(filter(lambda x: x % differ == 0, list(range(len(string)))))
    added = []
    for s in range(number):
        for i in range(len(string)):
            if i in start_inds and i not in added:
                output += string[i]
                added.append(i)

        temp_list = []
        for n in range(len(string)):
            if n + 1 in start_inds and n not in added:
                temp_list.append(n)
            elif n - 1 in start_inds and n not in added:
                temp_list.append(n)
        start_inds = temp_list[:]
    print(output)


if __name__ == "__main__":
    main()
```
