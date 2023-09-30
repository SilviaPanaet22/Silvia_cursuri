from datetime import datetime
import csv


def adauga_categorie(lista_categorii):
    print("Introduceți categoriile de taskuri (tastați \"stop\" pentru a încheia):")
    while True:
        categorie = input()
        if categorie.lower() == "stop":
            break
        elif categorie not in lista_categorii:
            lista_categorii.append(categorie)
        else:
            print("Categoria există deja.")
    return lista_categorii


def adauga_task(lista_categorii, lista_taskuri):
    while True:
        task = {'text': input("Introduceți un task: "),
                'data': input("Introduceți data limită a taskului (format: YYYY-MM-DD HH:MM): "),
                'persoana': input("Introduceți persoana responsabilă pentru task: ")}

        categorii_task = []
        while True:
            print(f"Categorii disponibile: {', '.join(lista_categorii)}")
            categorie_input = input("Introduceți o categorie din lista de mai sus sau tastați 'stop' pentru a încheia: ").lower()

            if categorie_input == "stop":
                break

            if categorie_input in lista_categorii:
                categorii_task.append(categorie_input)
            else:
                print(f"Categoria '{categorie_input}' nu există în lista de categorii. Vă rog introduceți o categorie validă.")

        task['categorie'] = categorii_task

        task_existent = next((t for t in lista_taskuri if t['text'] == task['text']), None)
        if task_existent:
            print("Taskul există deja, vă rog reformulați.")
        else:
            try:
                datetime.strptime(task['data'], "%Y-%m-%d %H:%M")
                lista_taskuri.append(task)
                print("Task adăugat cu succes!")
            except ValueError:
                print("Vă rog introduceți o dată validă, în formatul YYYY-MM-DD HH:MM.")

        adauga_alta = input("Doriți să adăugați alt task? (Da/Nu): ").lower()
        if adauga_alta != "da":
            break

    return lista_taskuri

def afiseaza_taskuri(lista_taskuri):
    if not lista_taskuri:
        print("Nu există task-uri.")
    else:
        for i, task in enumerate(lista_taskuri, start=1):
            print(f"{i}. Task: {task['text']}")
            print(f"   Data limită: {task['data']}")
            print(f"   Persoană responsabilă: {task['persoana']}")
            print(f"   Categorie: {task['categorie']}\n")


def main():
    categorii = []
    taskuri = []

    print("Bine ați venit în gestionarea listei de task-uri!")
    categorii = adauga_categorie(categorii)
    taskuri = adauga_task(categorii, taskuri)

    while True:
        print("\nMeniu:")
        print("1. Listare task-uri")
        print("2. Ieșire")

        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            afiseaza_taskuri(taskuri)
        elif optiune == "2":
            break
        else:
            print("Opțiune invalidă!")


if __name__ == "__main__":
    main()
