# ARTKEPS DEV MANUAL

**Tento dokument nie je dokončený a bude sa upravovať a dopĺňať v prípade potreby a po vzájomnej dohode členov tímu.**

## VERSIONING

V projekte sa používa názvoslovie založené na [Semantic Versioning](http://semver.org/).

## GIT

### GIT REPOZITÁR

Všetky zdrojové kódy sú uložené v repozitári [Git](http://github.com/). Repozitár je verejný a dostupný na
adrese projektu [ARTKEPS](https://github.com/TIS2022-FMFI/spektra).

### GIT BRANCHING

Každý člen tímu si vytvára vlastný branch, ktorý sa volá podľa issue, ktorú práve rieši.
Branch sa vytvorí z master branchu a po dokončení práce sa pushne do master branchu. Iný
člen tímu musí spraviť code review a prípadne potvrdiť merge request. Všetok kód z priečinku models
musí byť otestovaný a bez otestovania sa nesmie mergnúť do master branchu.

### GIT COMMIT MESSAGES

Commit message musí obsahovať krátke zhrnutie zmien, ktoré sú v commit-e.

## IMPLEMENTÁCIA

### VŠEOBECNE

Všetky zdrojové kódy sú písané v jazyku Python 3.9.*. Používame framework Qt, konkrétne jeho variant PySide6, ktorého
dokumentáciu nájdete na [PySide6](https://doc.qt.io/qtforpython/).
Na vykreslenie grafov používame knižnicu [PyQtGraph](https://pyqtgraph.readthedocs.io/en/latest/).

### ARCHITEKTÚRA A ORGANIZÁCIA KÓDU

Projekt používa architektúru MVC. Všetky zdrojové kódy sú rozdelené do priečinkov podľa ich funkcie.
Projekt obsahuje viaceré moduly, ktoré sú v priečinku **models**. Každý modul poskytuje zakladnú funkcionalitu,
ktorá je potrebná pre zabezpečenie základných činností aplikácie a musí byť otestovaná v prípade, že bola implementovaná
nanovo niekým z nášho tímu. Každý modul musí byť vytvorený ako trieda, ktorá poskytuje interface pre kontroler.
Kontroler je zodpovedný za komunikáciu medzi modulom a view. View je zodpovedný za zobrazenie dát, ktoré poskytuje
kontrolér. Všetok kód pre kontroléry sa nachádza v priečinku **controllers**. Všetok kód pre view sa nachádza v
priečinku **view**.
Všetky zdrojové kódy pre testovanie sa nachádzajú v priečinku **tests**. Errory definované pre tento projekt sa
nachádzajú
v priečinku **errors**. Uloženie dát z meraní sa nachádza v priečinku **saved_measurements**. V priečinku **assets** sa
nachádzajú
grafické zdroje pre aplikáciu. V priečinku **utils** sa nachádzajú pomocné funkcie, ktoré sú použité v rôznych moduloch.
Logovanie sa nachádza v priečinku **logs**. Priečinok **themes** obsahuje rôzne 'skiny', ktoré aplikácia môže použiť. V
súbore **settings** sa nachádza trieda, ktorá obsahuje nastavenia pre aplikáciu.
V súbore **main** sa nachádza spustiteľný kód pre aplikáciu.

### TESTOVANIE

Všetky zdrojové kódy, ktoré sa nachádzajú v priečinku **models** sú testované pomocou
knižnice [unittest](https://docs.python.org/3/library/unittest.html).
Testy sa nachádzajú v priečinku **tests**.
Každý člen tímu si musí vytvoriť testy pre všetky svoje zdrojové kódy, ktoré sa nachádzajú v priečinku **models**
ešte pred commitom. Všetky testy naraz sa spúšťajú z koreňového adresára pomocou príkazu `python -m unittest discover -s ./tests -p "main.py"`
.
Teda po napísaní testov je ich následne potrebné naimportovať do súboru **tests/main.py**.
Samozrejme, že testy sa musia aj spustiť a musia prejsť a...

### DOKUMENTÁCIA

Túto časť by mal dopísať člen tímu, ktorý má na starosti dokumentáciu...teda Sebo :)

### NÁZVY SÚBOROV, FUNKCIÍ, PREMENNÝCH...

Názvy súborov, funkcií, premenných, tried, atď. sa píšu v angličtine. Všetky stringy, ktoré majú byť zobrazené užívateľovi , sú napísané po slovensky. Po dohode viac lokalizácii nemusíme riešiť. Názvy súborov sa píšu v malých písmenách a
slová sú oddelené podtržítkom (snake case). Názvy tried sa píšu v camel case. Názvy funkcií a premenných sa píšu taktiež
v snake case. Názvy **ne**skracujeme, teda napr. namiesto `lvl` používame `level`. Názvy signálov majú postfix `_s`. Ak
uvidíte, že niekto v kóde použil iné názvoslovie, tak ho prosím refaktorujte.

### OSTATNÉ

1. Nepoužívajme `assert` na debugovanie mimo testov.
2. Nemažme kód ani nemenme funkcionalitu kódu niekoho iného bez jeho vedomia. Pokiaľ si myslím, že tam je chyba
   prípadne sa to dá vylepšiť, tak to napíšem do komentárov ako TODO / FIXME a požiadam člena tímu, aby to opravil.
3. ...dopíšte ďalšie pravidlá, ktoré vám napadnú a sú pre vás dôležité...
