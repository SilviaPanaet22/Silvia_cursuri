from datetime import datetime
import csv


def add_category(list_category: list) -> list:
    print("Introduceti categoriile de taskuri (introduceti \"stop\" pentru a va opri): ")
    while True:
        x = input()
        if x.lower() == "stop":
            break
        elif x not in list_category:
            list_category.append(x)
        else:
            print("Categoria exista deja.")
    return list_category


def add_task(list_category: list, list_task: list) -> list:
    while True:
        task = {'text': input("Introduceti taskul: "),
                'data': input("Introduceti data limita a taskului (format: YYYY-MM-DD HH:MM) : "),
                'persoana': input("Introduceti persoana responsabila pentru task: "),
                'categorie': input(f"Introduceti o categorie din care face parte taskul ({list_category}): ").lower()}
        while task['categorie'] not in list_category:
            task['categorie'] = input(
                f"Categoria aleasa nu exista. Va rog introduceti o categorie din lista ({list_category}): ").lower()
        check = False
        for value in list_task:
            if value['text'] == task['text']:
                check = True
        while check:
            task['text'] = input("Taskul exista deja, va rog reformulati: ")
            check = False
            for value in list_task:
                if value['text'] == task['text']:
                    check = True
        while True:
            try:
                datetime.strptime(task['data'], "%Y-%m-%d %H:%M")
                break
            except ValueError:
                task['data'] = input("Va rog introduceti o data valida, dupa formatul YYYY-MM-DD HH:MM: ")
        list_task.append(task)
        choice = input("Doriti sa continuati sa introduceti taskuri ? (Da/Nu): ").lower()
        while choice != "da" and choice != "nu":
            choice = input("Va rog alegeti Da sau Nu: ")
        if choice == "nu":
            break
    return list_task


def create_files(list_category: list, list_task: list) -> bool:
    with open("categorii.txt", 'w') as category_file:
        for value_category in list_category:
            category_file.write(value_category)
            category_file.write("\n")
    nume_header = ["Nr.", "Task", "Data limita", "Persoana responsabila", "Categorie"]
    with open("taskuri.csv", 'w', newline='') as task_file:
        writer = csv.DictWriter(task_file, fieldnames=nume_header)
        writer.writeheader()
        for index, row in enumerate(list_task):
            row_temp = {
                "Nr.": index + 1,
                "Task": row["text"],
                "Data limita": row["data"],
                "Persoana responsabila": row["persoana"],
                "Categorie": row["categorie"]
                }
            writer.writerow(row_temp)
    return True


def listare(list_task: list) -> bool:
    taskuri_sorted = sorted(list_task, key=lambda categorie: categorie['categorie'])
    for value in taskuri_sorted:
        print(' '.join(value_dict for value_dict in value.values()))
    return True


def sortare(list_task: list) -> bool:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Alegeti una din metodele de sortare: ")
    print("1. Sortare ascendentă task")
    print("2. Sortare descendentă task")
    print("3. Sortare ascendentă data")
    print("4. Sortare descendentă data")
    print("5. Sortare ascendentă persoana responsabilă")
    print("6. Sortare descendentă persoană responsabilă")
    print("7. Sortare ascendentă categorie")
    print("8. Sortare descendentă categorie")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice_sort = input()
    task_sortat = []
    if choice_sort == '1':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['text'])
    elif choice_sort == '2':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['text'], reverse=True)
    elif choice_sort == '3':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['data'])
    elif choice_sort == '4':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['data'], reverse=True)
    elif choice_sort == '5':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['persoana'])
    elif choice_sort == '6':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['persoana'], reverse=True)
    elif choice_sort == '7':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['categorie'])
    elif choice_sort == '8':
        task_sortat = sorted(list_task, key=lambda alegere: alegere['categorie'], reverse=True)
    else:
        print("Alegerea nu exista.")
    for value in task_sortat:
        print(' '.join(value_dict for value_dict in value.values()))
    return True


def filtrare(list_task: list) -> bool:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Alegeti campul dupa care doriti sa filtrati: ")
    print("1.Textul taskului.")
    print("2.Data limita.")
    print("3.Persoana responsabila.")
    print("4.Categorie.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice_camp = input()
    if choice_camp not in ['1', '2', '3', '4']:
        print("Alegerea nu exista.")
        return True
    filter_text = input("Introduceti filtrul: ")
    for value in list_task:
        if choice_camp == '1':
            if filter_text in value['text']:
                print(' '.join(value_dict for value_dict in value.values()))
        elif choice_camp == '2':
            if filter_text in value['data']:
                print(' '.join(value_dict for value_dict in value.values()))
        elif choice_camp == '3':
            if filter_text in value['persoana']:
                print(' '.join(value_dict for value_dict in value.values()))
        elif choice_camp == '4':
            if filter_text in value['categorie']:
                print(' '.join(value_dict for value_dict in value.values()))
    return True


def editare(list_category: list, list_task: list) -> list:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Alegeti taskul pe care doriti sa il editati: ")
    for index, value in enumerate(list_task):
        print(f"{index + 1}.{' '.join(value_dict for value_dict in value.values())}")
    choice_task = input()
    while choice_task.isdigit() is False or int(choice_task) not in range(1, len(list_task) + 1):
        choice_task = input("Alegerea nu exista, va rog alegeti din nou: ")
    choice_task = int(choice_task) - 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Alegeti campul pe care doriti sa il editati: ")
    print("1.Textul taskului.")
    print("2.Data limita.")
    print("3.Persoana responsabila.")
    print("4.Categorie.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice_camp = input()
    if choice_camp == '1':
        list_task[choice_task]['text'] = input("Introduceti taskul: ")
        check = False
        for value in list_task:
            if value['text'] == list_task[choice_task]['text']:
                check = True
        while check:
            list_task[choice_task]['text'] = input("Taskul exista deja, va rog reformulati: ")
            check = False
            for value in list_task:
                if value['text'] == list_task[choice_task]['text']:
                    check = True
    elif choice_camp == '2':
        list_task[choice_task]['data'] = input("Introduceti data limita a taskului (format: YYYY-MM-DD HH:MM) : ")
        while True:
            try:
                datetime.strptime(list_task[choice_task]['data'], "%Y-%m-%d %H:%M")
                break
            except ValueError:
                list_task[choice_task]['data'] = input(
                    "Va rog introduceti o data valida, dupa formatul YYYY-MM-DD HH:MM: ")
    elif choice_camp == '3':
        list_task[choice_task]['persoana'] = input("Introduceti persoana responsabila pentru task: ")
    elif choice_camp == '4':
        list_task[choice_task]['categorie'] = input(
            f"Introduceti o categorie din care face parte taskul ({list_category}): ").lower()
        while list_task[choice_task]['categorie'] not in list_category:
            list_task[choice_task]['categorie'] = input(
                f"Categoria aleasa nu exista. Va rog introduceti o categorie din lista ({list_category}): ").lower()
    else:
        print("Alegerea nu exista.")
    return list_task


def stergere(list_task: list) -> list:
    print("Alegeti taskul pe care doriti sa il stergeti: ")
    for index, value in enumerate(list_task):
        print(f"{index + 1}.{' '.join(value_dict for value_dict in value.values())}")
    choice = input()
    while choice.isdigit() is False or int(choice) not in range(1, len(list_task) + 1):
        choice = input("Alegerea nu exista, va rog alegeti din nou: ")
    choice = int(choice) - 1
    list_task.pop(choice)
    return list_task


taskuri = []
categorii = []
categorii = add_category(categorii)
taskuri = add_task(categorii, taskuri)
create_files(categorii, taskuri)
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Meniu taskuri. Alegeti operatiunea dorita: ")
    print("0.Inchidere meniu.")
    print("1.Listare date.")
    print("2.Listare date sortate.")
    print("3.Filtrare date.")
    print("4.Adauga un nou task.")
    print("5.Editeaza un task.")
    print("6.Sterge un task.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice_menu = input()
    if choice_menu == '0':
        break
    elif choice_menu == '1':
        listare(taskuri)
    elif choice_menu == '2':
        sortare(taskuri)
    elif choice_menu == '3':
        filtrare(taskuri)
    elif choice_menu == '4':
        taskuri = add_task(categorii, taskuri)
        create_files(categorii, taskuri)
    elif choice_menu == '5':
        taskuri = editare(categorii, taskuri)
        create_files(categorii, taskuri)
    elif choice_menu == '6':
        taskuri = stergere(taskuri)
        create_files(categorii, taskuri)
    else:
        print("Alegerea nu exista.")