'''
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
'''

import random

imena = [
    'Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka',
    'Antonio', 'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David',
    'Ivan', 'Petar', 'Marija', 'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej',
    'Jozo Matej', 'Petar', 'Ivan', 'Stjepan', 'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana',
    'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan', 'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano',
    'Mate', 'Mateo', 'Harun'
]

imenik = {}

for ime in imena:
    ocjena = random.randint(1, 5)
    imenik[ime] = ocjena

broj_ocjena = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

for ocjena in imenik.values():
    broj_ocjena[ocjena] += 1

prolaznost = sum(broj_ocjena[ocjena] 
                for ocjena in range(2, 6)) / len(imenik) * 100

print("Rezultati:")
print(imenik)
print("Broj ocjena od 1 do 5:")
print(broj_ocjena)
print("Postotak prolaznosti: {:.2f}%".format(prolaznost))



