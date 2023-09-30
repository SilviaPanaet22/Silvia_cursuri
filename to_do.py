import json


def citeste_categorii():
    try:
        with open("categorii.json", "r") as file:
            categorii = json.load(file)
    except FileNotFoundError:
        categorii = []

    return categorii


def salveaza_categorii(categorii):
    with open("categorii.json", "w") as file:
        json.dump(categorii, file)


def citeste_taskuri():
    try:
        with open("taskuri.json", "r") as file:
            taskuri = json.load(file)
    except FileNotFoundError:
        taskuri = []

    return taskuri


def salveaza_taskuri(taskuri):
    with open("taskuri.json", "w") as file:
        json.dump(taskuri, file)


def adauga_categorie():
    categorii = citeste_categorii()
    categoria = input("Introduceți o categorie: ")

    if categoria not in categorii:
        categorii.append(categoria)
        salveaza_categorii(categorii)
        print("Categorie adăugată cu succes!")
    else:
        print("Eroare: Categoria deja există!")


def adauga_task():
    categorii = citeste_categorii()
    taskuri = citeste_taskuri()

    task = input("Introduceți un task: ")
    data_limita = input("Introduceți data limită (ex: 22.01.2022 21:30): ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categorie = input("Introduceți categoria: ")

    if categorie not in categorii:
        print("Eroare: Categoria nu există!")
    elif any(t["task"] == task for t in taskuri):
        print("Eroare: Task deja existent!")
    else:
        task_nou = {
            "task": task,
            "data_limita": data_limita,
            "responsabil": responsabil,
            "categorie": categorie
        }
        taskuri.append(task_nou)
        salveaza_taskuri(taskuri)
        print("Task adăugat cu succes!")


def afiseaza_taskuri():
    taskuri = citeste_taskuri()

    if not taskuri:
        print("Nu există task-uri.")
    else:
        for i, task in enumerate(taskuri, start=1):
            print(f"{i}. Task: {task['task']}")
            print(f"   Data limită: {task['data_limita']}")
            print(f"   Persoană responsabilă: {task['responsabil']}")
            print(f"   Categorie: {task['categorie']}\n")


def main():
    while True:
        print("\nMeniu:")
        print("1. Adăugare categorie")
        print("2. Adăugare task")
        print("3. Afisează task-uri")
        print("0. Ieșire")

        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            adauga_categorie()
        elif optiune == "2":
            adauga_task()
        elif optiune == "3":
            afiseaza_taskuri()
        elif optiune == "0":
            break
        else:
            print("Opțiune invalidă!")


if __name__ == "__main__":
    main()
