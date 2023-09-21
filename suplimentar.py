# ... Codul existent până acum ...
# Creăm o listă pentru stocarea task-urilor
tasks = []

# Creăm o listă pentru stocarea categoriilor valide
categories = ["curs", "cumpărături", "muncă", "cadouri"]

# Definim o funcție pentru a adăuga un task
def adauga_task():
    task = input("Introduceți task-ul: ")
    data_limita = input("Introduceți data limită (ex. 22.01.2022 21:30): ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categorie = input("Introduceți categoria: ")

    # Verificăm dacă categoria este validă
    if categorie not in categories:
        print("Categorie invalidă. Categoriile valide sunt:", ", ".join(categories))
    else:
        tasks.append((task, data_limita, responsabil, categorie))

# Definim o funcție pentru afișarea task-urilor
def afiseaza_taskuri():
    print("\nTaskuri:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Task: {task[0]}")
        print(f"   Data limită: {task[1]}")
        print(f"   Persoana responsabilă: {task[2]}")
        print(f"   Categorie: {task[3]}")
        print()

# Definim o funcție pentru a salva task-urile într-un fișier
def salveaza_taskuri():
    with open("taskuri.txt", "w") as file:
        for task in tasks:
            file.write(f"Task: {task[0]}\n")
            file.write(f"Data limită: {task[1]}\n")
            file.write(f"Persoana responsabilă: {task[2]}\n")
            file.write(f"Categorie: {task[3]}\n\n")

# Definim funcția principală
def main():
    print("Introduceți categoriile de taskuri:")
    adauga_categorii = True
    while adauga_categorii:
        categorie = input("Introduceți o categorie (sau 'stop' pentru a încheia): ")
        if categorie.lower() == "stop":
            adauga_categorii = False
        else:
            categories.append(categorie)

    while True:
        adauga_task()
        raspuns = input("Doriți să adăugați un alt task? (da/nu): ")
        if raspuns.lower() != "da":
            break

    afiseaza_taskuri()
    salveaza_taskuri()

if __name__ == "__main__":
    main()
# Definim funcția pentru afișarea meniului
def afiseaza_meniu():
    print("\nMeniu:")
    print("1. Listare date")
    print("2. Sortare")
    print("3. Filtrare date")
    print("4. Adăugare task")
    print("5. Editare task")
    print("6. Ștergere task")
    print("7. Ieșire")


# Definim funcția pentru listarea datelor sortate după categorie
def listare_date_sortate():
    tasks.sort(key=lambda x: x[3])  # Sortăm după categorie
    afiseaza_taskuri()


# Definim funcția pentru sortarea datelor
def sortare_date(criteriu):
    criterii_sortare = {
        "1": lambda x: x[0],  # Sortare ascendentă după task
        "2": lambda x: x[0],  # Sortare descendentă după task
        "3": lambda x: x[1],  # Sortare ascendentă după data
        "4": lambda x: x[1],  # Sortare descendentă după data
        "5": lambda x: x[2],  # Sortare ascendentă după persoana responsabilă
        "6": lambda x: x[2],  # Sortare descendentă după persoana responsabilă
        "7": lambda x: x[3],  # Sortare ascendentă după categorie
        "8": lambda x: x[3],  # Sortare descendentă după categorie
    }
    tasks.sort(key=criterii_sortare[criteriu])
    afiseaza_taskuri()


# Definim funcția pentru filtrarea datelor
def filtrare_date(camp, valoare):
    tasks_filtrate = [task for task in tasks if valoare in task[camp - 1]]
    afiseaza_taskuri(tasks_filtrate)


# Definim funcția pentru adăugarea unui nou task
def adauga_nou_task():
    task = input("Introduceți noul task: ")
    # Verificăm dacă task-ul există deja în listă
    if any(task == existing_task[0] for existing_task in tasks):
        print("Task-ul există deja în listă.")
        return

    data_limita = input("Introduceți data limită (ex. 22.01.2022 21:30): ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categorie = input("Introduceți categoria: ")

    # Verificăm dacă categoria există deja în lista de categorii
    if categorie not in categories:
        print("Categorie invalidă. Categoriile valide sunt:", ", ".join(categories))
        return

    tasks.append((task, data_limita, responsabil, categorie))


# Definim funcția pentru editarea unui task existent
def editeaza_task():
    afiseaza_taskuri()
    try:
        indice = int(input("Introduceți numărul task-ului pe care doriți să-l editați: ")) - 1
        if 0 <= indice < len(tasks):
            print("Editare task:", tasks[indice][0])
            camp = input("Ce câmp doriți să editați (task/data/persoană/categorie)? ").strip().lower()
            if camp == "task":
                task_nou = input("Introduceți noul task: ")
                # Verificăm dacă task-ul există deja în listă
                if any(task_nou == existing_task[0] for existing_task in tasks if existing_task != tasks[indice]):
                    print("Task-ul există deja în listă.")
                    return
                tasks[indice] = (task_nou, tasks[indice][1], tasks[indice][2], tasks[indice][3])
            elif camp == "data":
                data_noua = input("Introduceți noua dată (ex. 22.01.2022 21:30): ")
                tasks[indice] = (tasks[indice][0], data_noua, tasks[indice][2], tasks[indice][3])
            elif camp == "persoană":
                persoana_noua = input("Introduceți noua persoană responsabilă: ")
                tasks[indice] = (tasks[indice][0], tasks[indice][1], persoana_noua, tasks[indice][3])
            elif camp == "categorie":
                categorie_noua = input("Introduceți noua categorie: ")
                # Verificăm dacă categoria există deja în lista de categorii
                if categorie_noua not in categories:
                    print("Categorie invalidă. Categoriile valide sunt:", ", ".join(categories))
                    return
                tasks[indice] = (tasks[indice][0], tasks[indice][1], tasks[indice][2], categorie_noua)
            else:
                print("Câmp invalid. Reîncercați cu 'task', 'data', 'persoană' sau 'categorie'.")
        else:
            print("Numărul task-ului introdus nu este valid.")
    except ValueError:
        print("Introduceți un număr valid pentru task.")


# Definim funcția pentru ștergerea unui task
def sterge_task():
    afiseaza_taskuri()
    try:
        indice = int(input("Introduceți numărul task-ului pe care doriți să-l ștergeți: ")) - 1
        if 0 <= indice < len(tasks):
            print("Ștergere task:", tasks[indice][0])
            confirmare = input("Doriți să continuați? (da/nu): ").strip().lower()
            if confirmare == "da":
                del tasks[indice]
                print("Task-ul a fost șters.")
        else:
            print("Numărul task-ului introdus nu este valid.")
    except ValueError:
        print("Introduceți un număr valid pentru task.")


# Funcția principală
def main():
    while True:
        afiseaza_meniu()
        optiune = input("Introduceți opțiunea dorită: ").strip()

        if optiune == "1":
            listare_date_sortate()
        elif optiune == "2":
            criteriu_sortare = input("Introduceți criteriul de sortare (1-8): ").strip()
            sortare_date(criteriu_sortare)
        elif optiune == "3":
            camp_filtrare = int(input("Introduceți câmpul de filtrare (1-4): ").strip())
            valoare_filtrare = input("Introduceți valoarea de filtrare: ").strip()
            filtrare_date(camp_filtrare, valoare_filtrare)
        elif optiune == "4":
            adauga_nou_task()
        elif optiune == "5":
            editeaza_task()
        elif optiune == "6":
            sterge_task()
        elif optiune == "7":
            print("Ieșire din program. Salvare în fișier...")
            salveaza_taskuri()
            break
        else:
            print("Opțiune invalidă. Reîncercați.")


if __name__ == "__main__":
    main()
