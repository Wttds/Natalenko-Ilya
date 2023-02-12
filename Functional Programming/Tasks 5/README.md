# Задание 5_1
Найти и вывести самую длиннуую подстроку, где ни один символ не повторяется.
# Листинг 5_1
```Py
def main():
    string = input()
    unique_letters = ''
    max_str = ''
    for i in range(len(string)):
        if string[i] not in unique_letters:
            unique_letters += string[i]
        else:
            if len(unique_letters) > len(max_str):
                max_str = unique_letters
            unique_letters = string[i]
    if len(unique_letters) > len(max_str):
        max_str = unique_letters
    print(max_str)


if __name__ == "__main__":
    main()
```
________
# Задание 5_2
Развернуть строку, убрав все лишние пробелы и сделать первую букву заглавной.
# Листинг 5_2
```Py
def main():
    arr = list(filter(lambda x: x, input().strip().split()))[::-1]
    print(' '.join(arr).capitalize())
    
    
if __name__ == "__main__":
    main()
```
________
# Задание 5_3
Проверить правильность введённых скобок. Если всё праивльно, вывести True. Если не всё правильно, вывести самую длинную подстроку с верной последовательностью. Если верных последовательностей нет, вывести False.
# Листинг 5_3
```Py

```
