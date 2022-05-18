import bottle
import model


TIPKOVNICA = [
    "QWERTZUIOPŠ",
    "ASDFGHJKLČŽ",
    "YXCVBNM"
]

vislice = model.Vislice()



@bottle.get("/img/<file>")
def staticne_slike(file):
    return bottle.static_file(file, root="img")

@bottle.get("/oblika/<file>")
def staticno_oblikovanje(file):
    return bottle.static_file(file, root="oblika")


@bottle.get("/")
def osnovno():
    return bottle.template("index")


@bottle.post("/igra/")
def nova_igra():
    nov_id = vislice.nova_igra()
    return bottle.redirect(f"/igra/{nov_id}")


@bottle.get("/igra/<id_igre:int>")
def pokazi_igro(id_igre):
    return bottle.template(
        "igra",
        id_igre=id_igre, igra=vislice.igre[id_igre][0],
        tipke=TIPKOVNICA)


def preveri_vnos(crka):
    return len(crka) == 1 and ("A" <= crka <= "Z" or crka in "ČŽŠ")


@bottle.post('/igra/<id_igre:int>')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka').upper()
    if preveri_vnos(crka):
        vislice.ugibaj(id_igre, crka)
        return pokazi_igro(id_igre)
    else:
        return f"<p>To ni dovoljena črka: {crka}</p>"


@bottle.post("/pretekle_igre/")
def pokazi_pretekle_igre():
    igre = vislice.igre
    return bottle.template("pretekle_igre", igre=igre)
        


bottle.run(reloader=True, debug=True)
