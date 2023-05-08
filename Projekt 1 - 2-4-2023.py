
######### 1. Mé kontaktní údaje: ##########

# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Filip
# email: 479@seznam.cz
# discord: Filip479#8140


# ########## Texty možné analyzovat: ##########

TEXTS = ["""

Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. 
""",

"""
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
"""]


# ########## Registrovaní uživatelé a jejich hesla: ##########
print("\n")

passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass321"
    }

# ########## 2. Vyžádá si od uživatele přihlašovací jméno a heslo ##########
print("Ahoj, toto je analyzátor textů \n")
user = input("-"*50 + "\nZadej své přihlašovací jméno a stiskni [Enter]: \n")
if user in passwords:
    print("\nAhoj", user)
    password = input("Zadej své přihlašovací heslo a stiskni [Enter]: \n")
else:
    print("-"*50 + "\nNeregistrovany uzivatel \nProgram se ukončil.")
    quit()

# ########## 3. Zjistí, jestli zadaný je uživatel registrovaný ##########
if user in passwords and password == passwords[user]:
    print("\n")

########## 4. Pokud je registrovaný, umožni mu analyzovat texty ##########
    print("Vítej", user, "zde jsou tři texty, které můžeš analyzovat:")

# ########## 5A. Pokud není registrovaný, ukonči program ##########
else:
    print("-"*50 + "\nNesprávné heslo \nProgram se ukončil.")
    quit()

for radek in TEXTS:
    ciste_texty = "\n".join([radek.strip() for radek in radek.splitlines()])
    # ciste_texty = "".join([radek.strip() for radek in radek.splitlines()])
    print("-"*50)
    print(ciste_texty)


# ########## 5B. Program nechá uživatele vybrat mezi třemi TEXTS ##########
print("-"*50)
vyber = int(input("\n" + "Vyber text 1, 2, nebo 3 a stiskni [Enter]: \n"))


# ########## 6. Pro vybraný text spočítá následující statistiky: ##########
# počet slov,
# počet slov začínajících velkým písmenem,
# počet slov psaných velkými písmeny,
# počet slov psaných malými písmeny,
# počet čísel (ne cifer),
# sumu všech čísel (ne cifer) v textu.

if vyber in range(1, 4):
# if vyber in range(1, 4) and vyber.isdigit():
    print(f"\nVybral/a jsi Text", vyber,":" "\n" + "-"*50, (TEXTS[vyber-1]))
    print("\n\n" + "\t"*2 + "ZDE JE ANALÝZA VYBRANÉHO TEXTU")

    pocet_slov = (TEXTS[vyber-1]).split()
    count = len(pocet_slov)
    print(f"\nPočet slov (včetně čísel) je: ", count)
    print("-"*60)

    pocet_slov_sVelkym = (TEXTS[vyber-1]).split()
    count_sVelkym = 0
    for slovo_sVelkym in pocet_slov_sVelkym:
        if slovo_sVelkym[0].isupper():
            count_sVelkym += 1
    print(f"Počet slov začínajících velkým písmenem je: ", count_sVelkym)
    print("-"*60)
    
    pocet_slov_VELKYMI = (TEXTS[vyber-1]).split()
    count_VELKYMI = 0
    for slovo_VELKYMI in pocet_slov_VELKYMI:
        if slovo_VELKYMI[0:].isupper():
            count_VELKYMI += 1
    print(f"Počet slov psaných velkými písmenemy je: ", count_VELKYMI)
    print("-"*60)

    pocet_cisel = (TEXTS[vyber-1]).split()
    count_cisel = 0
    for cisla in pocet_cisel:
        if cisla.isnumeric():
            count_cisel += 1
    print(f"Počet čísel (samostatných, bez jednotek) je: ", count_cisel)
    print("-"*60)

    soucet_cisel = (TEXTS[vyber-1]).split()
    count_soucet = 0
    for cisla in soucet_cisel:
        if cisla.isnumeric():
            count_soucet += int(cisla)
    print(f"Součet čísel (samostatných, bez jednotek) je: ", count_soucet)
    print("-"*60)
    
else:
    print("Neplatná volba, lze zadat jen čísla: 1, 2, nebo 3")
    print("Program se ukončil\n")
    print("-"*50)
    quit()


# ########## 7. Program zobrazí jednoduchý sloupcový graf,
#   který bude reprezentovat četnost různých délek slov v textu ##########
vycistena_slova = []

for slovo in (TEXTS[vyber-1]).split():
    ciste_slovo = slovo.strip(",.!?:")
    vycistena_slova.append(ciste_slovo.lower())
# print(vycistena_slova)
# ############################################################################
vyskyt_slov = {}

for slovo in vycistena_slova:
    if slovo not in vyskyt_slov:
        vyskyt_slov[slovo] = 1
    else:
        vyskyt_slov[slovo] += 1
# print(vyskyt_slov)
# ############################################################################
pet_nejcastejsich = []

nejcastejsi_hodnoty = sorted(list(vyskyt_slov.values()), reverse = True)[0:]

vyskyt = int()
for vyskyt_slov in vyskyt_slov:
    if vyskyt_slov[vyskyt] in nejcastejsi_hodnoty:
        pet_nejcastejsich.append(vyskyt_slov[vyskyt])
# print(nejcastejsi_hodnoty)
# ############################################################################
print("\n\n\tZDE JE ZNÁZORNĚNA ČETNOST DÉLEK SLOV:")

delka_slov = {}

for slovo in (TEXTS[vyber-1]).split():
    delka = len(slovo)
    if delka in delka_slov:
        delka_slov[delka] += 1
    else:
        delka_slov[delka] = 1
# print(delka_slov)
# ############################################################################
delka_slov = dict(sorted(delka_slov.items()))

print("- "*30)
print("Délka slova | Znazorneni poctu | Počet slov")
for delka, count in sorted(delka_slov.items()):
    hvezdicky = "*" * delka
    print(f"{delka:>11} | {hvezdicky:<16} | {count}")
print("-"*60)

print("\n"*2 + "-"*60)
print("\nJsme rádi, že jsi využil/a náš analyzátor textů\nPěkný den !")
print("\n"*2 + "-"*60)
