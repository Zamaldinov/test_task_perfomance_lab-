def collect_result():
    start = 0
    while True:
        end_index = (m + start) % n - 1
        val = num_list[end_index]
        if val == 1:
            break
        result.append(val)
        start = end_index


n = int(input('Введите размер массива: '))
m = int(input('Введите размер шага: '))
result = []
num_list = list(range(1, n + 1))
result.append(num_list[0])

collect_result()
print(f'Полученный путь: {result}')
