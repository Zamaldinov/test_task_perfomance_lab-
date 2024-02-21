import sys


def collect_result(list_len, step):
    start = 0
    while True:
        end_index = (step + start) % list_len - 1
        val = num_list[end_index]
        if val == 1:
            break
        result.append(val)
        start = end_index


argument_list = sys.argv[1:]
n = int(argument_list[0])
m = int(argument_list[1])
result = []
num_list = list(range(1, n + 1))
result.append(num_list[0])

collect_result(n, m)
print(f'Полученный путь: {result}')
