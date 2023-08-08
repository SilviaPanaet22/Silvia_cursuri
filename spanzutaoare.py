#onomatopee
cuvant = 'onomatopee'.lower()
cuvant_de_ghicit = list(cuvant)
for i, v in enumerate(cuvant):
    if cuvant_de_ghicit[0] != v and cuvant_de_ghicit[-1] !=v:
        cuvant_de_ghicit[i] = '_'
cuvant_de_afisat = ' '.join(cuvant_de_ghicit)
print(cuvant_de_afisat)
nr_total_vieti = 7
litere_incercare = set()
while nr_total_vieti > 0:
    litera=input("Alege o litera: ").lower()
    if len(litera) != 1:
        print('Te rog introdu un singur caracter!')
        continue
    if not litera.isalpha():
        print('Te rog introdu litere!')
        continue
    if litera in cuvant:
        for i, v in enumerate(cuvant):
            if litera == v:
                cuvant_de_ghicit[i] = litera
        cuvant_de_afisat = ' '.join(cuvant_de_ghicit)
        print(cuvant_de_afisat)
        if '_' not in cuvant_de_ghicit:
            print("Ai castigat !")
            break
    else:
        if litera not in litere_incercare:
            litere_incercare.add(litera)
            nr_total_vieti -= 1
            if(nr_total_vieti == 0):
                print(f'Ai pierdut! Cuvantul era: {cuvant}')
                break
            else:
                print(f'Vieti ramase: {nr_total_vieti}.')
        print(f"Lista literelor incercate este: {', '.join(litere_incercare)}")