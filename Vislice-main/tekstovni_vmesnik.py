from model import nova_igra


def izpis_igre(igra):
    return f"TRENUTNO STANJE: {igra.pravilni_del_gesla()}"


def izpis_zmage(igra):
    return f"BRAVO, ODKRITA BESEDA JE {igra.geslo}"


def izpis_poraza(igra):
    return f"IZGUBIL SI TO IGRO. BESEDA JE BILA {igra.geslo}"


def pozeni_vmesnik():
    igra = nova_igra()
    while True:
        crka = input("UGIBAJ ČRKO: ")
        igra.ugibaj(crka)
        print(izpis_igre(igra))
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
        else:
            izpis_igre(igra)


pozeni_vmesnik()