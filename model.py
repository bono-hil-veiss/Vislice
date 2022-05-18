import random
import uuid


def pripravi_bazen():
    with open("besede.txt", encoding="utf-8") as f:
        return [vrsta.strip() for vrsta in f.readlines()]


BAZEN_BESED = pripravi_bazen()
STEVILO_DOVOLJENIH_NAPAK = 10
ZACETEK = "zacetek"
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = '-'
ZMAGA, PORAZ = 'W', 'X'


class Igra:
    def __init__(self, geslo):
        self.geslo = geslo.upper()
        self.crke = set()

    def pravilne_crke(self):
        return [x for x in self.crke if x in self.geslo]

    def napacne_crke(self):
        return [x for x in self.crke if x not in self.geslo]

    def stevilo_napak(self):
        return min(len(self.napacne_crke()), STEVILO_DOVOLJENIH_NAPAK)

    def zmaga(self):
        return len(self.pravilne_crke()) == len(set(self.geslo))

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        return " ".join(c if c in self.crke else "_" for c in self.geslo)

    def nepravilni_ugibi(self):
        return ", ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.add(crka)
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


def nova_igra():
    return Igra(random.choice(BAZEN_BESED))


class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        # return len(self.igre)
        while True:
            kandidat = uuid.uuid4().int
            if kandidat not in self.igre:
                return kandidat

    def nova_igra(self):
        igra = nova_igra()
        novi_id = self.prost_id_igre()
        self.igre[novi_id] = (igra, ZACETEK)
        return novi_id

    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)


