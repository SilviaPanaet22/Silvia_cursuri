""" r-> citim, nu adaugam, daca fisierul nu exista, apare eroare
     w, scriere, daca fisierul """
#with open("data.txt", "r"):
with open("data.txt", "w") as item:
    item.write("hello")
