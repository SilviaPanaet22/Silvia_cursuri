from datetime import datetime
import csv

def input_categories(categories_list: list) -> list:
    print("Introduceti categoriile de taskuri (introduceti \"stop\" pentru a va opri): ")
    while True:
        category = input()
        if category.lower() == "stop":
            break
        elif category not in categories_list:
            categories_list.append(category)
        else:
            print("Categoria exista deja.")
    return categories_list

def input_task(categories_list: list, tasks_list: list) -> list:
    while True:
        task = {'text': input("Introduceti taskul: "),
                'deadline': input("Introduceti data limita a taskului (format: YYYY.MM.DD HH:MM): "),
                'responsible_person': input("Introduceti persoana responsabila pentru task: "),
                'category': input(f"Introduceti o categorie din care face parte taskul ({categories_list}): ").lower()}
        while task['category'] not in categories_list:
            task['category'] = input(
                f"Categoria aleasa nu exista. Va rog introduceti o categorie din lista ({categories_list}): ").lower()
        check = False
        for value in tasks_list:
            if value['text'] == task['text']:
                check = True
        while check:
            task['text'] = input("Taskul exista deja, va rog reformulati: ")
            check = False
            for value in tasks_list:
                if value['text'] == task['text']:
                    check = True
        while True:
            try:
                datetime.strptime(task['deadline'], "%Y.%m.%d %H:%M")
                break
            except ValueError:
                task['deadline'] = input("Va rog introduceti o data valida, dupa formatul YYYY.MM.DD HH:MM: ")
        tasks_list.append(task)
        choice = input("Doriti sa continuati sa introduceti taskuri ? (Da/Nu): ").lower()
        while choice != "da" and choice != "nu":
            choice = input("Va rog alegeti Da sau Nu: ")
        if choice == "nu":
            break
    return tasks_list

def create_files(categories_list: list, tasks_list: list) -> bool:
    with open("categorii.txt", 'w') as category_file:
        for value_category in categories_list:
            category_file.write(value_category)
            category_file.write("\n")
    nume_header = ["Nr.", "Task", "Data limita", "Persoana responsabila", "Categorie"]
    with open("taskuri.csv", 'w', newline='') as task_file:
        writer = csv.DictWriter(task_file, fieldnames=nume_header)
        writer.writeheader()
        for index, row in enumerate(tasks_list):
            row_temp = {
                "Nr.": index + 1,
                "Task": row["text"],
                "Data limita": row["deadline"],
                "Persoana responsabila": row["responsible_person"],
                "Categorie": row["category"]
            }
            writer.writerow(row_temp)
    return True

def list_tasks(tasks_list: list) -> bool:
    tasks_sorted = sorted(tasks_list, key=lambda task: task['category'])
    for value in tasks_sorted:
        print(' '.join(value_dict for value_dict in value.values()))
    return True

def sort_tasks(tasks_list: list) -> bool:

    print("Alegeti o metoda de sortare: ")
    print("1. Sortare ascendentă task")
    print("2. Sortare descendentă task")
    print("3. Sortare ascendentă data")
    print("4. Sortare descendentă data")
    print("5. Sortare ascendentă persoana responsabila")
    print("6. Sortare descendentă persoană responsabila")
    print("7. Sortare ascendentă categorie")
    print("8. Sortare descendentă categorie")

    choice_sort = input()
    task_sorted = []
    if choice_sort == '1':
        task_sorted = sorted(tasks_list, key=lambda task: task['text'])
    elif choice_sort == '2':
        task_sorted = sorted(tasks_list, key=lambda task: task['text'], reverse=True)
    elif choice_sort == '3':
        task_sorted = sorted(tasks_list, key=lambda task: task['deadline'])
    elif choice_sort == '4':
        task_sorted = sorted(tasks_list, key=lambda task: task['deadline'], reverse=True)
    elif choice_sort == '5':
        task_sorted = sorted(tasks_list, key=lambda task: task['responsible_person'])
    elif choice_sort == '6':
        task_sorted = sorted(tasks_list, key=lambda task: task['responsible_person'], reverse=True)
    elif choice_sort == '7':
        task_sorted = sorted(tasks_list, key=lambda task: task['category'])
    elif choice_sort == '8':
        task_sorted = sorted(tasks_list, key=lambda task: task['category'], reverse=True)
    else:
        print("Alegerea nu exista.")
    for value in task_sorted:
        print(' '.join(value_dict for value_dict in value.values()))
    return True

def filter_tasks(tasks_list: list) -> bool:

    print("Alegeti campul dupa care doriti sa filtrati: ")
    print("1. Textul taskului.")
    print("2. Data limita.")
    print("3. Persoana responsabila.")
    print("4. Categorie.")

    choice_camp = input()
    if choice_camp not in ['1', '2', '3', '4']:
        print("Alegerea nu exista.")
        return True
    filter_text = input("Introduceti filtrul: ")
    for value in tasks_list:
        if choice_camp == '1':
            if filter_text in value['text']:
                print(' '.join(value_dict for value_dict in value.values()))
        elif choice_camp == '2':
            if filter_text in value['deadline']:
                print(' '.join(value_dict for value_dict in value.values()))
        elif choice_camp == '3':
            if filter_text in value['responsible_person']:
                print(' '.join(value_dict for value_dict in value.values()))
        elif choice_camp == '4':
            if filter_text in value['category']:
                print(' '.join(value_dict for value_dict in value.values()))
    return True

def edit_task(categories_list: list, tasks_list: list) -> list:

    print("Alegeti taskul pe care doriti sa il editati: ")
    for index, value in enumerate(tasks_list):
        print(f"{index + 1}.{' '.join(value_dict for value_dict in value.values())}")
    choice_task = input()
    while choice_task.isdigit() is False or int(choice_task) not in range(1, len(tasks_list) + 1):
        choice_task = input("Alegerea nu exista, va rog alegeti din nou: ")
    choice_task = int(choice_task) - 1

    print("Alegeti numarul pe care doriti sa il editati: ")
    print("1. Textul taskului.")
    print("2. Data limita.")
    print("3. Persoana responsabila.")
    print("4. Categorie.")

    choice_camp = input()
    if choice_camp == '1':
        tasks_list[choice_task]['text'] = input("Introduceti taskul: ")
        check = False
        for value in tasks_list:
            if value['text'] == tasks_list[choice_task]['text']:
                check = True
        while check:
            tasks_list[choice_task]['text'] = input("Taskul exista deja, va rog reformulati: ")
            check = False
            for value in tasks_list:
                if value['text'] == tasks_list[choice_task]['text']:
                    check = True
    elif choice_camp == '2':
        tasks_list[choice_task]['deadline'] = input("Introduceti data limita a taskului (format: YYYY.MM.DD HH:MM): ")
        while True:
            try:
                datetime.strptime(tasks_list[choice_task]['deadline'], "%Y.%m.%d %H:%M")
                break
            except ValueError:
                tasks_list[choice_task]['deadline'] = input(
                    "Va rog introduceti o data valida, dupa formatul YYYY.MM.DD HH:MM: ")
    elif choice_camp == '3':
        tasks_list[choice_task]['responsible_person'] = input("Introduceti persoana responsabila pentru task: ")
    elif choice_camp == '4':
        tasks_list[choice_task]['category'] = input(
            f"Introduceti o categorie din care face parte taskul ({categories_list}): ").lower()
        while tasks_list[choice_task]['category'] not in categories_list:
            tasks_list[choice_task]['category'] = input(
                f"Categoria aleasa nu exista. Va rog introduceti o categorie din lista ({categories_list}): ").lower()
    else:
        print("Alegerea nu exista.")
    return tasks_list

def delete_task(tasks_list: list) -> list:
    print("Alegeti taskul pe care doriti sa il stergeti: ")
    for index, value in enumerate(tasks_list):
        print(f"{index + 1}.{' '.join(value_dict for value_dict in value.values())}")
    choice = input()
    while choice.isdigit() is False or int(choice) not in range(1, len(tasks_list) + 1):
        choice = input("Alegerea nu exista, va rog alegeti din nou: ")
    choice = int(choice) - 1
    tasks_list.pop(choice)
    return tasks_list

tasks = []
categories = []
categories = input_categories(categories)
tasks = input_task(categories, tasks)
create_files(categories, tasks)
while True:

    print("Meniu- Alegeti operatiunea dorita: ")
    print("0. Inchidere meniu.")
    print("1. Listare date.")
    print("2. Listare date sortate.")
    print("3. Filtrare date.")
    print("4. Adauga un nou task.")
    print("5. Editeaza un task.")
    print("6. Sterge un task.")

    choice_menu = input()
    if choice_menu == '0':
        break
    elif choice_menu == '1':
        list_tasks(tasks)
    elif choice_menu == '2':
        sort_tasks(tasks)
    elif choice_menu == '3':
        filter_tasks(tasks)
    elif choice_menu == '4':
        tasks = input_task(categories, tasks)
        create_files(categories, tasks)
    elif choice_menu == '5':
        tasks = edit_task(categories, tasks)
        create_files(categories, tasks)
    elif choice_menu == '6':
        tasks = delete_task(tasks)
        create_files(categories, tasks)
    else:
        print("Alegerea nu exista.")
