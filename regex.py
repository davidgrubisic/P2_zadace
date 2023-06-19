'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

ime_prezime = input("Unesite ime i prezime: ")

regex = r'^D[a-z0-5\s]*G$'

if re.match(regex, ime_prezime):
    print("Podudara se.")
else:
    print("Unos se ne podudara sa uvjetima.")

