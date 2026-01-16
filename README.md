# Přírodou inspirované algoritmy &ndash; cvičení

Tento repozitář obsahuje materiály ke cvičením z Přírodou inspirovaných algoritmů ([NAIL119](https://is.cuni.cz/studium/predmety/index.php?do=predmet&kod=NAIL119)) vedeným [Matyášem Lorencem](https://kam.mff.cuni.cz/~lorenc/).

Materiály jsou rozdělené do složek po jednotlivých tématech, tak jak jsou procházeny na hodinách. V každé složce se nachází [Jupyter Notebook](https://jupyter.org/) s ukázkou látky z daného tématu, případně potřebná podkladová data nebo suplementární soubory s kódem.

Veškerý kód je psaný v [Pythonu](https://www.python.org/). V každé složce se též nachází soubor `requirements.txt` s knihovnami potřebnými pro seběhnutí příslušného kódu. Stejně tak je zde na kořenové úrovni k dispozici soubor `all_requirements.txt`, v němž jsou tyto jednotlivé požadavky shrnuty v jednom souboru. Můžete tak buď mít jedno virtuální prostředí pro každou hodinu, nebo jedno společné pro celý kurz &ndash; požadované knihovny by neměly být v konfliktu.

(Pozn.: Pro některá témata využívající knihovnu [TensorFlow](https://www.tensorflow.org/) by se Vám mohla hodit podpora GPU, bez níž běží kód výrazně pomaleji (i když i bez ní seběhne). Byť je zprovoznění TensorFlow na vašem případném grafickém procesoru netriviální &ndash; kor třeba oproti v těchto materiálech nevyužívanému konkurenčnímu [PyTorchi](https://pytorch.org/) (jejž bych Vám v případě dalšího zájmu o neuronové sítě radil spíše používat) &ndash; doporučuji Vám pokusit se to učinit. I kdyby jen jako lekci v tom, co vlastně akcelerace na grafických kartách požaduje, a bližší seznámení se s ní.)

Dále se v některých podsložkách vyskytují soubory `optional_requirements.txt`, jež obsahují knihovny, které nejsou nutné pro hlavní funkcionalitu kódu, ale odemykají jeho některé možnosti. Vyžadují ovšem instalaci dalšího softwaru bokem (toto je dále rozváděno v jednotlivých příslušných Jupyter Notebook souborech). Nainstalujete-li volitelné knihovny bez podkladového softwaru, příslušný kód v daném Notebooku bude vyhazovat chybu. Pokud knihovny nenainstalujete, Notebook vás jen upozorní, že na daném místě by byla k dispozici daná funkcionalita, ale vy ji nemáte zprovozněnou. Všechny tyto volitelné požadavky jsou opět shrnuty na kořenové úrovni repozitáře v souboru `optional_requirements.txt`.

Nakonec je Vám v kořenové úrovni tohoto repozitáře k dispozici i skript `get_code.py` (vyžaduje pipem instalovaný package `jupyter`), který Vám umožní extrahovat z libovolného vstupního Jupyter Notebooku Pythonní kód z kódových buňek daného Notebooku do jednoho `.py` souboru, aniž byste ho museli postupně vykopírovávat.

Pokud byste v kódu, textech, kdekoli našli nějakou chybu, nepřesnost, něco by se Vám nezdálo, nebojte se ozvat cvičícímu. Budete mít malé, zato však bezvýznamné plus za pomoc s korekcí materiálů.

UPOZORNĚNÍ: Běžný postup zde je, že před dalším rokem výuky se tento repozitář smaže, aby byl zas nahrazen novým, plněným doplňujícími materiály u jednotlivých témat postupně v průběhu semestru. Chcete-li si tedy některý jeho obsah ponechat pro další využití, stáhněte si ho před tímto promazáním.