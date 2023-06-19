'''
Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
'''

def generiraj_brojeve(n):
    for broj in range(n):
        if broj % 2 == 0:
            yield broj, "paran broj"
        else:
            yield broj, "neparan broj"
            
n = int(input("Unesite gornju granicu: "))

for broj, tip_broja in generiraj_brojeve(n):
    print(f"{broj} je {tip_broja}.")
