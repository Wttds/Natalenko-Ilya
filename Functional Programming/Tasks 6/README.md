# Задание 6_1
Задается количество элементов в списке ( >4). Задается целочисленный список длины N. Задается цель. Необходимо найти сумму 4 чисел, которые равны цели или находятся близко к ней и вывести их.  
Input:

N = 5

[1, 2, 4, -5,-2] 

C = 1

Output:

[1,2,4,-5]

2

Input:  

N = 6

[4, -5, -7, 12,-2,5]

C = -5

Output:

[4,-5,-7,5]

-3

Input:  

N = 7

[1,1,1,1,1,1,1]

C = 5

Output:

[1,1,1,1]

4

Input:  

N = 5

[1,3,0,-4,8]

C = 3

Output:

[1,0,-4,8]

5
# Листинг 6_1
```Py
def main():
    number = int(input())
    bin_nums = []
    for i in range(2 ** number):
        binary = format(i, "b")
        while len(binary) < number:
            binary = '0' + binary
        if binary.count('1') == 4:
            bin_nums.append(binary)
    print(bin_nums)

    arr = eval(input())
    aim = int(input())
    closest = None
    closest_arr = []
    for comb in bin_nums:
        summary, temp = 0, []
        for d in range(number):
            if comb[d] == '1':
                summary += arr[d]
                temp.append(arr[d])
        if not closest:
            closest, closest_arr = abs(aim - summary), temp[:]
        else:
            distance = abs(aim - summary)
            if distance < closest:
                closest, closest_arr = distance, temp[:]
    print(closest_arr, sum(closest_arr), sep='\n')


if __name__ == "__main__":
    main()
```
________
# Задание 6_2
Задается список целых чисел. Вывести список разделенный списками со всеми возможными уникальными перестановками целых чисел из заданного списка.
Input:

[1,2,3]

Output:

[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input:

[1,1,2]

Output:

[[1,1,2], [1,2,1], [2,1,1]]

Input:

[0]

Output:

[[0]]

# Листинг 6_2
```Py
from itertools import permutations


def main():
    items, output = eval(input()), []
    for x in permutations(items):
        x = list(x)
        if x not in output:
            output.append(x)
    print(output)


if __name__ == '__main__':
    main()
```
________
# Задание 6_3
Задается список строк.  Необходимо сгруппировать их в общий список по двум критериям:

1) слова имеют одни и те же буквы

2) слова одинаковой размерности

Input:

["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]

Output:

[['qwe', 'ewq'], ['asd', 'dsa'], ['dsas'], ['qwee'], ['zxc', 'cxz'], ['xxz'], ['z'], ['s'], ['qweasdzxc'], ['zzxc']]

Input

["a","a",""]

Output:

[['a', 'a'], ['']]
# Листинг 6_3
```Py
from itertools import permutations


def main():
    items, output = eval(input()), []
    for item in items:
        marker = False
        for array in output:
            for variant in permutations(array[0]):
                variant = ''.join(list(variant))
                if item in variant and len(item) == len(array[0]):
                    marker = True
                    array.append(item)
                    break
        if not marker:
            output.append([item])
    print(output)


if __name__ == "__main__":
    main()
```
________
