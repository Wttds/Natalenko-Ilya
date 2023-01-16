# Задание 9_1
Вы санта. Вы попросили эльфа вернуть вам список пользователей, где каждый пользователь представляет собой еще один список, который содержит один или два элемента: строка (имя пользователя) и его почтовый индекс. Пример:

[["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
! У одного пользователя есть имя, но нет индекса.

Напишите функцию santa_users(), которая принимает двумерный список, и возвращает словарь с элементом для каждого пользователя, где ключ - это имя пользователя, а значение - почтовый индекс пользователя. Если нет индекса, тогда значение должно быть None.

Например, santa_users() вернет этот словарь:

{
    "name1 surname1": 12345,
    "name2 surname2": None,
    "name3 surname3": 12354,
    "name4 surname4": 12435,    
}

# Листинг 9_1
```Py
def main():
    array = eval(input())
    # [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 21345], ["name4 surname4", 41325]]

    def santa_users(massive):
        dictionary = {}
        for pos in massive:
            if len(pos) == 2:
                dictionary[pos[0]] = pos[1]
            else:
                dictionary[pos[0]] = None
        return dictionary

    print(santa_users(array))


if __name__ == "__main__":
    main()
```
________
# Задание 9_2

# Листинг 9_2
```Py

```
________
# Задание 9_3

# Листинг 9_3
```Py

```
