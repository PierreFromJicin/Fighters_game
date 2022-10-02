import random

"""
Hra:
Predstavte si, ze jsem vas zakaznik a chci od Vas vytvorit v Pythonu hru simulaci areny s bojovniky.
Kreativite se meze nekladou, ale zakladni koncept je, ze mezi sebou budou souperit dva bojovnici na zivot a na smrt.

Programujte postupne reseni podle obtiznost:
Dva bojovnici mezi sebou bojuji na zivot a na smrt
Zapojte prvky nahody (nahodne bonusove poskozeni, ..)
Bojovnici budou bojovat v arene (Vytvorte arenu jako objekt)
Vytvorte vice druhu bojovniku s ruznymi vlastnostmi (sermir, lukostrelec, mag, ..)
"""


class Bojovnik:

    def __init__(self, jmeno, zbran, pocet_zivotu, stit: bool, bojove_zkusenosti):
        self.jmeno = jmeno
        self.zbran = zbran
        self.pocet_zivotu = pocet_zivotu
        self.stit = stit
        self.bojove_zkusenosti = bojove_zkusenosti
        self.sila_zbrane = self.ucinnost_zbrane()

        self.zbrane = {"mec": 75, "dyka": 50,
                       "kopi": 80, "palcat": 45, "maceta": 70}

    def ucinnost_zbrane(self):
        if self.zbran == "mec":
            ef_zbr = random.randrange(50, 76)
        elif self.zbran == "dyka":
            ef_zbr = random.randrange(15, 36)
        elif self.zbran == "kopi":
            ef_zbr = random.randrange(40, 96)
        elif self.zbran == "palcat":
            ef_zbr = random.randrange(15, 45)
        elif self.zbran == "maceta":
            ef_zbr = random.randrange(40, 76)
        else:
            ef_zbr = random.randrange(1, 11)

        return ef_zbr

    def jmeno(self):
        return self.jmeno

    def utok(self):
        return (random.randint(0, 100) + self.zbrane.get(self.zbran) + self.bojove_zkusenosti) / 3

    def obrana(self):
        return (random.randint(0, 100) + self.bojove_zkusenosti + (100 * self.stit)) / 3 * self.pocet_zivotu / 100

    def uder(self, protivnik):
        protivnik.pocet_zivotu -= self.sila_zbrane*random.random()
        if protivnik.pocet_zivotu <= 0:
            protivnik.pocet_zivotu = 0


def fight(*fighters):
    _fighterJ, _fighterR = fighters

    while _fighterJ.pocet_zivotu > 0 or _fighterR.pocet_zivotu > 0:

        if _fighterR.pocet_zivotu != 0:
            _fighterR.uder(_fighterJ)
            print(f"životy {_fighterJ.jmeno} {_fighterJ.pocet_zivotu: .1f}")

            if _fighterJ.pocet_zivotu != 0:
                _fighterJ.uder(_fighterR)
                print(f"životy {_fighterR.jmeno} {_fighterR.pocet_zivotu: .1f}")

            else:
                break
        else:
            break

    if _fighterR.pocet_zivotu != _fighterJ.pocet_zivotu:
        if _fighterR.pocet_zivotu != 0:
            winner = _fighterR.jmeno
        else:
            winner = _fighterJ.jmeno
    else:
        winner = "no_one"

    return winner


def arena(fighter_a, fighter_b):
    fighters: tuple = (fighter_a, fighter_b)
    #  TODO - dodělat vnesení náhodného výběru kdo zaútočí jako první
    arena_winner = fight(fighters[1], fighters[0])
    return arena_winner


Robin_bojovnik = Bojovnik("Robin", "mec", 100, True, 100)
Jan_bojovnik = Bojovnik("Jan", "mec", 100, True, 100)

ucinnost_zbrane = Robin_bojovnik.sila_zbrane
print("Robinova zbran: ", ucinnost_zbrane)
ucinnost_zbrane = Jan_bojovnik.sila_zbrane
print("Janova zbran: ", ucinnost_zbrane)

winner_name = arena(Robin_bojovnik, Jan_bojovnik)
print("The winner is: ", winner_name)

"""
# TODO - arena obsahuje funkci boj,
#  vstupy: styl boje (KO nebo počet zápasů), počet bojovníků, jména bojovníků,
#  náhoda určí kdo bude útočit a kdo se bude bránit,
#  funkce boj vrátí hodnoty úbytku zdraví (ve stylu KO bude prováděna až do úplného vyčerpání života jednoho bojovníka)
#  výstupy: kdo je vítěz, kolik má života, kdo je poražený a kolik má života

class Arena:

    def __init__(self, styl_boje = "KO", pocet_bojovniku, *jmena):
        self.styl = styl_boje
        self.pocet = pocet_bojovniku
        self.seznam_bojovniku = {}






def boj(bojovnik1, bojovnik2):
    hodnota_utoku = bojovnik1.utok()
    hodnota_obrany = bojovnik2.obrana()
    print(hodnota_obrany, hodnota_utoku)
    if hodnota_obrany > hodnota_utoku:
        bojovnik1.pocet_zivotu = bojovnik1.pocet_zivotu-(hodnota_obrany-hodnota_utoku)/10
        print(f"Vyhral {bojovnik2.jmeno} {(hodnota_obrany-hodnota_utoku)}")
    elif hodnota_utoku > hodnota_obrany:
        bojovnik2.pocet_zivotu = bojovnik2.pocet_zivotu-(hodnota_utoku-hodnota_obrany)/10
        print(f"Vyhral {bojovnik1.jmeno} {hodnota_utoku-hodnota_obrany}")
    else:
        print("Remiza")

boj(Robin_bojovnik, Jan_bojovnik)
print(Robin_bojovnik.pocet_zivotu, Jan_bojovnik.pocet_zivotu)
"""
