"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka
jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""
#Otetaan kuukausi nro
#Katsotaan mihin vuodenaikaan kuukausi kuuluu.
    #12, 1, 2 = Talvi [0]
    #3, 4, 5 = Kevät [1]
    #6, 7, 8 = Kesä [2]
    #9, 10, 11 = Syksy [3]
#Vuodenajat tuplesta otetaan syötetty kuukausinro ja palautetaan vastaava vuodenaika.
#Print vuodenaika

import math

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
kuukausi = int(input("Anna kuukauden numero (1 - 12): "))

if kuukausi == 12:
    vuodenaikanro = 0
else:
    vuodenaikanro = math.floor(kuukausi/3)


print (vuodenajat[vuodenaikanro])
