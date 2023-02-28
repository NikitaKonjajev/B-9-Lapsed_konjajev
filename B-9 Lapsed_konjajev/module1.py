import random
def lapsed(nimed, keskmised_hinnad, a):
    for i in range(a):
        nimi=input("Kirjuta lapse nimi: ")
        hinne=random.randint(2, 5)
        nimed.append(nimi)
        keskmised_hinnad.append(hinne)
    return nimed, keskmised_hinnad

def alf_nimed(nimed, keskmised_hinnad):
    sort_nimed = sorted(nimed)
    print("Lapsed nimid:")
    for i in range(len(sort_nimed)):
        index = nimed.index(sort_nimed[i])
        print(f"{sort_nimed[i]} - {keskmised_hinnad[index]}")

def otlichnik(keskmised_hinnad,nimed):
    if 5 in keskmised_hinnad:
        index = keskmised_hinnad.index(5)
        print(f"Viiemees: {nimed[index]}")
    else:
        print("Pole viiemeest")

def keskmine(keskmised_hinnad):
    Keskmine = sum(keskmised_hinnad) / len(keskmised_hinnad)
    print(f"Keskmine hind on: {Keskmine}")

def imja(nimed, keskmised_hinnad):
    nimi=input("Kirjuta lapse nimi: ")
    if nimi in nimed:
        index = nimed.index(nimi)
        kesk= keskmised_hinnad[index]
        print(f"kesk hind õpilasel on: {kesk}")
    else:
        print("Ei ole see last")

def oma(nimi1,arv1,nimed, keskmised_hinnad):
    nimed.append(nimi1)
    keskmised_hinnad.append(arv1)   
    return(nimed,keskmised_hinnad)
print()