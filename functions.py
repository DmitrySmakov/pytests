documents = [
    {"type": "passport",
     "number": "2207 876234",
     "name": "Василий Гупкин"},
    {"type": "invoice",
     "number": "11-2",
     "name": "Геннадий Покемонов"},
    {"type": "insurance",
     "number": "10006",
     "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['2207 876234']
}


# ввод/проверка документа
def input_document():
    flag = True
    document = input('Введите номер документа: ')
    while flag:
        temp = set()
        for doc in documents:
            temp = temp | set(doc.values())
        if document in temp:
            flag = False
        else:
            document = input('Нет документа с таким номером. Введите еще раз : ')
    return document


# p спросит номер документа документа выведет имя человека
def get_people():
    document = input_document()
    for doc in documents:
        if doc['number'] == document:
            print(doc['name'])
            return doc['name']

def get_people1(document):
    for doc in documents:
        if doc['number'] == document:
            # print(doc['name'])
            return doc['name']



# # s – shelf – выдаст номер полки по номеру документа
def get_shelf():
    document = input_document()
    for key, value in directories.items():
        if document in value:
            # !!print('Номер полки :', key)
            return key

def get_shelf1(document):
    # document = input_document()
    for key, value in directories.items():
        if document in value:
            # !!print('Номер полки :', key)
            return key

# # l– list – команда, которая выведет список всех документов
def print_documets():
    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    print()


########## ввод / проверка полки
def input_shelf():
    flag = True
    shield = input('Введите номер полки :')
    while flag:
        if shield in (directories.keys()):
            flag = False
        else:
            shield = input('Такой полки нет. введите снова :')
    return shield


# # a – add –  добавление нового документа
def add_document():
    inp_type = input('Введите тип документа :')
    # сделать : проверка если документ уже есть??? input_document()
    inp_doc = input('Введите номер документа :')
    inp_name = input('Введите Фамилию и имя :')
    to_dir = input_shelf()

    new_doc = {}
    new_doc['type'] = inp_type
    new_doc['number'] = inp_doc
    new_doc['name'] = inp_name
    documents.append(new_doc)

    directories[to_dir].append(inp_doc)

def add_document1(inp_type,inp_doc, inp_name ,to_dir ,documents,directories ):
    # inp_type = input('Введите тип документа :')
    # # сделать : проверка если документ уже есть??? input_document()
    # inp_doc = input('Введите номер документа :')
    # inp_name = input('Введите Фамилию и имя :')
    # to_dir = input_shelf()

    new_doc = {}
    new_doc['type'] = inp_type
    new_doc['number'] = inp_doc
    new_doc['name'] = inp_name
    documents.append(new_doc)
    directories[to_dir].append(inp_doc)

    return new_doc

################ удаляет документ /возвращает удаленный номер
def del_document():  # def del_document(document):
    document = input_document()
    for i in reversed(range(len(documents))):
        # if documents[i]['number'] == document:
        if document in list(documents[i].values()):
            del documents[i]

    for key, value in directories.items():
        if document in list(value):
            a = list(value)
            a.remove(document)
            directories[key] = a
    return document

def del_document1(document, documents, directories):  # def del_document(document):
    # document = input_document()
    for i in reversed(range(len(documents))):
        # if documents[i]['number'] == document:
        if document in list(documents[i].values()):
            del documents[i]

    for key, value in directories.items():
        if document in list(value):
            a = list(value)
            a.remove(document)
            directories[key] = a
    return document


#########################
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
def move_doc():
    document = input_document()
    for key, value in directories.items():
        if document in list(value):
            a = list(value)
            a.remove(document)
            directories[key] = a

    shelf = input_shelf()
    temp = directories[shelf]
    temp.append(document)
    directories[shelf] = temp
    return


##########################
def add_shelf():
    flag = True
    shelf = input('Введите номер новой полки : ')
    while flag:
        if shelf not in directories.keys():
            directories[shelf] = []
            print('Полка добавлена.')
            flag = False  # break
        else:
            shelf = input('Такая полка уже есть, введите снова : ')
            print()
    return shelf


##########################
def main():
    flag = True
    while flag:
        command = input('Введите команду p, s, l, a, d, m, as , dir,  quit: ')
        print()
        if command == 'p':
            get_people()  # print(get_people())
        elif command == 's':
            print()
            get_shelf()
        elif command == 'l':
            print_documets()
        elif command == 'a':
            add_document()
        elif command == 'd':
            del_document()
        elif command == 'm':
            move_doc()
        elif command == 'as':
            add_shelf()
        elif command == 'dir':
            for i, y in directories.items():
                print(i, y)
            print()
        elif command == 'quit':
            flag = False
        else:
            print(' Нет такой команды')


func_dict = {'p': get_people, 's': get_shelf, 'l': print_documets, 'q': False}  # q for quit program


def userChoice():  # def userChoice(self):
    y = True
    while y:
        choice = input("p. run P\ns. run S\nl. run L\nq. Quit").lower()
        if choice == "q":
            y = False
        else:
            func_dict[choice]()  # ?  почему это работает ? get_people + ()
        # self.func_dict[choice]()


# main()