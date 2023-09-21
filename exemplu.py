def main():

    try:

        numar = int(input("Introduceți un număr întreg pozitiv: "))



        if numar <= 0 or numar > 20:

            print("Vă rugăm să introduceți un număr întreg pozitiv mai mic sau egal cu 20.")

            return



        dictionar = {}



        for i in range(1, numar + 1):

            dictionar[i] = i**2



        print("Dicționarul rezultat:")

        for cheie, valoare in dictionar.items():

            print(f"Cheie: {cheie}, Valoare: {valoare}")



    except ValueError:

        print("Vă rugăm să introduceți un număr întreg pozitiv valid.")



if __name__ == "__main__":

    main()