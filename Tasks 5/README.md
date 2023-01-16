# Задание 5_1

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

# Листинг 5_2
```Py

```
________
# Задание 5_3

# Листинг 5_3
```Py

```
