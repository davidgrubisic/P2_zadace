'''
Podatke iz datoteke rezultati.csv učitati kao listu ntorki oblika (ime, prezime, bodovi).
Iterirati kroz sve studente i ispisati samo one koji su položili ispit (br. bodova veci od 49)
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.
Nedovoljan
0-49%
Dovoljan
50-65%
Dobar
65-80%
Vrlodobar
80-90%
Izvrstan
90-100%
'''


from csv import reader

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple, csv_reader))

studenti.sort(key=lambda el: el[1])

rjecnik_ocjena = {}

def rang_ocjene(bodovi):
    if bodovi >= 90:
        return 'Izvrstan'
    elif bodovi >= 80:
        return 'Vrlodobar'
    elif bodovi >= 65:
        return 'Dobar'
    elif bodovi >= 50:
        return 'Dovoljan'
    else:
        return 'Nedovoljan'

for student in studenti:
    prezime = student[1]
    bodovi = int(student[2])
    rang = rang_ocjene(bodovi)
    
    if rang in rjecnik_ocjena:
        rjecnik_ocjena[rang] += 1
    else:
        rjecnik_ocjena[rang] = 1

print(studenti)
print(rjecnik_ocjena)