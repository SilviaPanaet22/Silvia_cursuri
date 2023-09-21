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
