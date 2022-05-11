from re import X
from tkinter import W


STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = W
PORAZ = X

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return self.stevilo_napak() <= 10 and (crka for crka in self.geslo if crka in self.crke) == (crka for crka in self.geslo)

    def poraz(self):
        return self.stevilo_napak > 10

    def pravilni_del_gesla(self):
        rezultat = ''
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                rezultat += crka
            else:
                rezultat += '_'
        return rezultat 

    def nepravilni_ugibi(self):
        pass
