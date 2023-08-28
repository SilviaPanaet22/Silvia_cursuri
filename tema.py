numar = int(input("Introduceti un numar intreg: ")) #introduc  un numar intreg

if numar % 3 == 0 and numar % 5 == 0: # verific daca numarul este divizibil cu 3 și cu 5 si afisez mesajul
    print("FizzBuzz")
elif numar % 3 == 0: # verific daca numarul este divizibil cu 3 și afisez mesajul
    print("Fizz")
elif numar % 5 == 0: # verific daca numarul este dizivibil cu 5 și afisez mesajul
    print("Buzz")
else:
    print(numar) # in caz ca nu se indeplinesc conditiile de mai sus, afisez numarul introdus
