# Задание 7_1
Вы хотите ограбить банки вдоль улицы, которые идут подряд. В каждом банке есть сейф, в котором лежим определенная сумма денег ( в миллионах рублей). 
Так же в каждом банке есть система защиты, которая сработает если были ограблены два ближайших банка. 
На вход поступает количество банков на улице. Далее пользователь вводит (по мере их расположения): название банка и сумма денег в сейфе. 
Вам необходимо вернуть максимальную сумму денег,  которую вы можете получить (так чтобы не сработала сигнализация), название банков и их порядковые номера на улице.
# Листинг 7_1
```Py
def main():
    banks = []                                                                      # Создание списка банков
    num_of_banks = int(input())
    names = input().split()
    sums = input().split()
    for i in range(num_of_banks):
        banks.append((names[i], i, int(sums[i])))

    bin_nums = []                                                                   # Варианты ходов в бинарном виде
    for i in range(2 ** num_of_banks):
        binary = format(i, "b")
        while len(binary) < num_of_banks:
            binary = '0' + binary
        if '11' not in binary and '000' not in binary and '1' in binary and \
                not binary.startswith('00') and not binary.endswith('00'):
            bin_nums.append(binary)

    max_b = []
    max_i = []
    max_s = 0
    for combination in bin_nums:
        chosen_b = []
        chosen_i = []
        chosen_s = 0
        for digit in range(len(combination)):
            if combination[digit] == '1':
                chosen_b.append(banks[digit][0])
                chosen_i.append(banks[digit][1])
                chosen_s += banks[digit][2]
        if chosen_s > max_s:
            max_b, max_i, max_s = chosen_b[:], chosen_i[:], chosen_s
    print(max_b, max_i, max_s, sep='\n')


if __name__ == "__main__":
    main()
```
________
# Задание 7_2
Поворот матрицы по часовой стрелке.
# Листинг 7_2
```Py
def f(matrix):
    transposed_matrix = []
    for i in range(len(matrix)):
        transposed_matrix.append([])
        for j in range(len(matrix)):
            transposed_matrix[i].append(matrix[len(matrix) - 1 - i][j])
    print(transposed_matrix)

    reversed_matrix = []
    for i in range(len(matrix)):
        reversed_matrix.append([])
        for g in range(len(matrix)):
            reversed_matrix[i].append(transposed_matrix[g][i])
    return reversed_matrix


if __name__ == "__main__":
    print(f([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
```
________
# Задание 7_3

# Листинг 7_3
```Py

```
