from math import *
from random import *
from module1 import *

#B-9 Lapsed
nimed=[]
keskmised_hinnad=[]
a=int(input("Kirjuta laste arv: "))
print(lapsed(nimed, keskmised_hinnad, a))

while True:
    print("1 - Näitab ekraanile laste nimed, mis on järjestatud A-st Z-ni veergudesse (Nimi-Hindamine)")
    print("2 - Näitab suurepärast, kui see on olemas, kui seda ei kuvata")
    print("3 - Leia keskmine hinnang laste keskmistele hinnetele")
    print("4 - Leida lapse keskmine hinnang, märkides tema nime")
    print("5 - Hindamisnimekirja lisamine ja nimi")
    print("6 - välja")
    valik=input("Vali number: ")
    if valik=="1":
        alf_nimed(nimed, keskmised_hinnad)
    elif valik=="2":
        otlichnik(keskmised_hinnad,nimed)
    elif valik=="3":
        keskmine(keskmised_hinnad)
    elif valik=="4":
        imja(nimed, keskmised_hinnad)
    elif valik=="5":
        nimi1=input("Kirjuta nimi, mida sa tahad lisada: ")
        arv1=input("Kirjuta arv: ")
        print(oma(nimi1,arv1,nimed, keskmised_hinnad))
    elif valik=="6":
         break