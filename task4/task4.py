import sys


def count_step(num_list: list) -> int:
    num_int_list = [int(num) for num in num_list if num.isdigit()]
    sorted(num_int_list)
    middle = len(num_int_list) // 2
    mid_num = num_int_list[middle]
    result = 0
    for i in num_int_list:
        if i > mid_num:
            result += i - mid_num
        else:
            result += mid_num - i
    return result


argument_list = sys.argv[1:]
with open(argument_list[0], 'r') as file:
    numbers = file.read().split('\n')

res = count_step(numbers)
print(f'Минимальное количество ходов: {res}')
