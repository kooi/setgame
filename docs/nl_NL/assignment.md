# maakSet() en isSet() in python

## Algemene instructie

 - Ga naar [SetGame online](http://kooi.github.io/setgame).
 - Onder `code` kun je de code vinden staat de code, de eerste keer moet je deze wel inladen met _revert to default_.
 - Kijk goed naar wat de functies teruggeven (dit zie je naast het kaartenveld).
 - Je mag de code binnen `maakSet()` (of voor aanpassen, niet erbuiten;
 - als je dat gedaan hebt klik je apply patch om het toe te passen (als je code niet te begrijpen is krijg je een foutmelding; code tussen de twee `"""` is toelichting, lees deze goed door;
 - test je code na elke aanpassing;
 - code wordt automatisch opgeslagen in je browser dus je bent het niet kwijt als je de pagina herlaadt;
 - als je je code helemaal verpest kun je met revert to default weer terug naar het begin. Je bent je eigen aanpassingen dan wel kwijt;
 - lever telkens je code op moodle zodra je de opdracht gedaan hebt.


## Opdrachten maakSet()

 1. Laat `maakSet()` de kaart `[1, 1, 2, 3]` teruggeven.

 2. Laat `maakSet()` de eerste kaart die je aangeklikt hebt teruggeven. 
 
    >De kaarten `kaart1` en `kaart2` worden aan de functie meegegeven, dit kun je zien aan de regel `def maakSet(self, kaart1, kaart2)`. Deze objecten kun je dus gebruiken binnen `maakSet()` (en dus met `return`).

 3. Laat `maakSet()` de hoeveelheid van de eerste kaart teruggeven en de rest van de eigenschappen 0.

    >De eigenschappen van de aangeklikte kaarten kun je opvragen met `kaart1.hoeveelheid`, `kaart1.kleur`, `kaart1.vorm`, `kaart1.vulling` en `kaart2.hoeveelheid`, `kaart2.kleur`, `kaart2.vorm`, `kaart2.vulling`.

 4. Laat `maakSet()` de correcte hoeveelheid teruggeven en de rest 0.

    > Er zijn twee situaties waar je rekening mee moet houden:
    >  1. als de twee kaarten dezelfde hoeveelheid hebben en;
    >  2. als dat niet zo is (en ze dus allemaal verschillend zijn).
    >_Hint: Wat weet je in dit geval over de som van alle hoeveelheden van de 3 kaarten in een set?_

 5. Laat `maakSet()` de correcte kaart teruggeven (dus niet alleen de correcte hoeveelheid).

    > Deze lijkt heel veel op de vorige opdracht, maar nu voor alle eigenschappen; het is het makkelijkst als je al deze eigenschappen apart bepaalt.


## Opdracht isSet()

 6. Laat `isSet()` bepalen of de 3 aangeklikte kaarten samen een set zijn.

    > Je kunt je eigen `maakSet()` uit de vorige opdracht hergebruiken door binnen `isSet()` die functie aan te roepen met `self.maakSet()`.
    > Je kunt een hele kaart ook vergelijken met een andere kaart door `==` te gebuiken, dus met `if kaart1 == kaart2:` etc.
