'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
Istražiti greedy i non-greedy quantifiers.
'''


import re

email_regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
eduID_regex = r"^[a-zA-Z][a-zA-Z0-9]*X?@sum\.ba$"

email = input("Unesite e-mail adresu: ")
eduID = input("Unesite eduID: ")

if re.match(email_regex, email):
    print("Ispravan unos e-mail adrese.")
else:
    print("Neispravan unos e-mail adrese.")

if re.match(eduID_regex, eduID):
    print("Ispravan unos eduID-a.")
else:
    print("Neispravan unos eduID-a.")
