'''
Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.
'''

def string_unazad(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + string_unazad(string[:-1])
string = input("Unesite string: ")
print("String ispisan sa zada: ")
ispis_stringa = string_unazad(string)
print(ispis_stringa)