documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def whose_number_doc():
    while True:
        number_doc = input('Введите номер документа: ')
        if exit_q(number_doc):  # Выход к main функции
            return
        for doc in documents:
            if number_doc == doc['number']:
                print(doc['name'])
                return
        else:
            print('Такого документа нет')


def which_shelf():
    while True:
        number_doc = input('Введите номер документа: ')
        if exit_q(number_doc):  # Выход к main функции
            return
        for number_shelf, docs_list in directories.items():
            if number_doc in docs_list:
                print(f'Документ на {number_shelf} полке')
                return
        else:
            print('Такого документа нет')


def all_docs():
    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')


def add_doc():
    while True:
        number_shelf = input('Введите номер полки, на которой будет расположен документ: ')
        if exit_q(number_shelf):  # Выход к main функции
            return
        if number_shelf in directories.keys():
            number_doc = input('Введите номер документа: ')
            if exit_q(number_doc):  # Выход к main функции
                return
            type_doc = input('Введите тип документа: ')
            if exit_q(type_doc):  # Выход к main функции
                return
            owners_name = input('Введите имя владельца документа: ')
            if exit_q(owners_name):  # Выход к main функции
                return
            new_doc_dict = {"type": type_doc, "number": number_doc, "name": owners_name}
            documents.append(new_doc_dict)
            directories[number_shelf].append(number_doc)
            break
        else:
            print('Такой полки нет')


def delete_doc():
    while True:
        number_doc = input('Введите номер документа: ')
        if exit_q(number_doc):  # Выход к main функции
            return
        for doc in documents:
            if number_doc == doc['number']:
                documents.remove(doc)
        for doc in directories.values():
            if number_doc in doc:
                doc.remove(number_doc)
                return
        else:
            print('Такого документа нет')


def move_doc():
    while True:
        number_doc = input('Введите номер документа: ')
        if exit_q(number_doc):  # Выход к main функции
            return
        old_num_shelf = check_doc_in_shelves(number_doc)
        if not old_num_shelf:
            print('такого документа нет')
            continue
        while True:
            number_shelf = input('Введите номер полки, куда переместить: ')
            if exit_q(number_shelf):  # Выход к main функции
                return
            if not check_shelf(number_shelf):
                print('такой полки нет')
                continue
            directories[old_num_shelf].remove(number_doc)
            directories[number_shelf].append(number_doc)
            return


def check_doc_in_shelves(num_doc):
    for k, v in directories.items():
        if num_doc in v:
            return k
    return 0


def check_shelf(num_shelf):
    for shelf in directories:
        if num_shelf == shelf:
            return True
    return 0


def add_shelf():
    while True:
        number_shelf = input('Введите номер полки: ')
        if exit_q(number_shelf):  # Выход к main функции
            return
        if check_shelf(number_shelf):
            print('Такая полка уже существует')
            continue
        directories[number_shelf] = []
        return


def exit_q(command):
    if command == 'q':
        return 1
    return 0


def main():
    """
        Список доступных команд:
        p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        l – list – команда, которая выведет список всех документов;
        a – add – команда, которая добавит новый документ в каталог и в перечень полок;
        d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
        m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
        as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.

    """

    command_dict = {
        'p': whose_number_doc,
        's': which_shelf,
        'l': all_docs,
        'a': add_doc,
        'd': delete_doc,
        'm': move_doc,
        'as': add_shelf,
    }
    while True:
        command = input('Введите команду: ')
        if exit_q(command):  # Выход к main функции
            break
        elif command in command_dict.keys():
            command_dict[command]()
        else:
            print('Такой команды нет')


main()
