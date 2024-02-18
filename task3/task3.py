import json


def tests(tests_dict: list, values_dict: dict) -> list:
    """Функция проходит по списку и в каждом найденном словаре вставляет значения
    соответствующего id"""
    for i_index in tests_dict:
        if isinstance(i_index, list):
            for j in i_index:
                tests(j, values_dict)
        keys = i_index.keys()
        if 'value' in keys and 'id' in keys:
            i_index['value'] = values_dict[i_index['id']]
        if 'values' in keys:
            tests(i_index['values'], values_dict)
    return tests_dict


def new_dict(test_dict):
    """Собираем новый словарь состоящий из id:value"""
    id_value = {}
    for i_index in test_dict:
        id_value[i_index['id']] = i_index['value']
    return id_value


with open('tests.json') as file:
    data_tests = json.load(file)

with open('values.json') as file:
    data_values = json.load(file)

id_value_dict = new_dict(data_values['values'])
result = tests(data_tests['tests'], id_value_dict)

with open('report.json', 'w') as file:
    json.dump(result, file, indent=4)
