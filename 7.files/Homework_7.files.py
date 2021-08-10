from pprint import pprint


def filter_cook_txt(file_name):
    cook_dict = dict()
    with open(file_name) as f:
        while True:
            dish_name = f.readline().strip()
            cook_dict[dish_name] = list()
            number = int(f.readline())
            while number != 0:
                ingredient_list = f.readline().split('|')
                cook_dict[dish_name].append({
                    'ingredient_name': ingredient_list[0].strip(),
                    'quantity': ingredient_list[1].strip(),
                    'measure': ingredient_list[2].strip()
                })
                number -= 1
            if f.readline() == '':
                return cook_dict


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    cook_book_dict = cook_book
    result_dict = dict()
    intersection_dishes = set(dishes).intersection(set(cook_book_dict.keys()))
    absence_dishes = set(dishes) - set(cook_book_dict.keys())
    if absence_dishes:
        print('Таких блюд нет:', absence_dishes)
    for dish in intersection_dishes:
        for ingredient_dict in cook_book_dict[dish]:
            result_dict[ingredient_dict['ingredient_name']] = {
                'measure': ingredient_dict['measure'],
                'quantity': int(ingredient_dict['quantity']) * person_count
            }
    return result_dict


# pprint(get_shop_list_by_dishes(filter_cook_txt('recipes.txt'), ['Запеченный картофель', 'Омлет'], 2))


def_list = ['1.txt', '2.txt', '3.txt']


def fix_list(default_list):
    count_dict = dict()
    for file in default_list:
        count = 0
        with open(file) as f:
            for string in f:
                count += 1
        count_dict[file] = count
    return sorted(count_dict, key=count_dict.get)[:3]


def connect_files(fixed_list):
    files_name_list = fixed_list
    for file in files_name_list:
        with open(file) as f:
            data = f.readlines()
        with open('../result.txt', 'a') as f:
            f.write(f'{file}\n')
            f.write(f'{str(len(data))}\n')
            f.write(''.join(data) + '\n')


# connect_files(fix_list(def_list))

