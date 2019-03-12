# Wyrażenia regularne

Wyrażenia regularne pokazane są na przykładzie implementacji w języku Python 3 w module `re`.


## Znaki specjalne

Większość znaków może być używana jako literały. Istnieją jednak znaki specjalne, które muszą być poprzedzone ukośnikiem \, aby można było ich używać jako literałów. Wspomniane znaki specjalne to: \ . ^ $ ? + * { } [ ] |


## Klasy znaków
Jeśli chcemy dopasować jeden znak z określonego zbioru znaków należy użyć klasy znaków. Klasa znaków to jeden lub większa liczba znaków ujętych w nawiasy kwadratowe. Klasa znaków jest wyrażeniem. Jeśli nie jest podany po niej kwantyfikator, zostanie dopasowany dokładnie jeden znak spośród znaków zdefiniowanych w klasie znaków.
Dla częstych klas znaków dostępne są poniższe skróty.

| Klasa znaków | Dopasowanie                                     |
|--------------|-------------------------------------------------|
| .	           | Dowolny znak z wyjątkiem znaku nowej linii      |
| \d	         | Dowolna cyfra                                   |
| \D	         | Dowolna znak nie będący cyfrą                   |
| \s	         | Dowolny biały znak                              |
| \S	         | Dowolny znak nie będący białym znakiem          |
| \w	         | Dowolny znak alfanumeryczny (litera lub cyfra)  |
| \W	         | Dowolny znak nie będący znakiem alfanumerycznym |


## Kwantyfikatory wyrażeń regularnych

Kwantyfikatory określają ilość powtórzeń znaków lub sekwencji we wzorcach. Domyślnie kwantyfikatory są zachłanne, tzn. starają się dopasować maksymalną możliwą ilość znaków w tekście.

|Kwantyfikator	| Dopasowanie |
| --- | ---|
|* | 0 lub więcej wystąpień |
|+ | 1 lub więcej wystąpień |
|? | 0 lub 1 wystąpienie |
|{m} | dokładnie m wystąpień |
|{m,} | co najmniej m wystąpień |
|{,n} | co najwyżej n wystąpień |
|{m,n} | od m do n wystąpień |
|[...] | jeden znak spośród zbioru znaków |
|[^...] | jeden znak spoza zbioru znaków |
|A \| B | dopasowanie A lub B, operator alternatywy jest zachłanny |

## Kwantyfikatory niezachłanne
Dodanie znaku zapytania po kwantyfikatorze przekształca go w kwantyfikator niezachłanny (leniwy). Kwantyfikator niezachłanny stara się dopasować minimalną możliwą ilość tekstu.

| Kwantyfikator |	Dopasowanie |
| --- | --- |
| *? | 0 lub więcej wystąpień, wersja niezachłanna |
| +? | 1 lub więcej wystąpień, wersja niezachłanna |
| ?? | 0 lub 1 wystąpienie, wersja niezachłanna |
| {m,n}? | od m do n wystąpień, wersja niezachłanna |

## Asercje
Asercje (kotwice) pozwalają wyznaczyć miejsce w tekście, w którym musi pojawić się dopasowanie. Asercje mają w dopasowaniu zerową długość.

| Asercja | Dopasowanie |
| --- | --- |
| ^ | 	początek tekstu, także początek nowej linii w przypadku włączonej opcji re.MULTILINE
| $ | koniec tekstu, także koniec nowej linii w przypadku włączonej opcji re.MULTILINE |
| \A | początek tekstu |
| \Z | koniec tekstu |
| \b | pusty string na początku lub końcu słowa (dopasowuje granicę słowa albo początek lub koniec tekstu) |
| \B | pusty string, lecz nie na początku lub końcu słowa (dopasowanie wewnątrz słowa)
| (?=e) | dopasowuje łańcuch, jeśli bezpośrednio po nim następuje wyrażenie pasujące do e (ang. positive lookeahead) |
| (?!e) | dopasowuje łańcuch, jeśli bezpośrednio po nim nie następuje wyrażenie pasujące do e (ang. negative lookeahead) |
| (?<=e) | dopasowuje łańcuch, jeśli bezpośrednio przed nim następuje wyrażenie pasujące do e (ang. positive lookebehind) |
| (?<!e) | dopasowuje łańcuch, jeśli bezpośrednio przed nim nie następuje wyrażenie pasujące do e (ang. negative lookebehind) |

W przypadku asercji wstecznych (ang. lookbehind) implementacja dla Pythona dopuszcza skończoną i ustaloną długość wzorca e. Zatem użycie operatora Kleen'a * lub operatora zakresu {n,m} jest niedozwolone w asercji wstecznej.

## Surowe ciągi znaków

Surowe ciągi znaków (ang. `raw strings`) ułatwiają pisanie wyrażeń regularnych w Pythonie, zmniejszając potrzebę użycia znaków ukośnika (backslash'a). Łańcuch znaków poprzedza się literą r, która wyłącza specjalne znaczenie ukośnika. Dobrą praktyką jest zawsze definiowanie wzorców jako surowych łańcuchów.

Przykłady zwykłych łańcuchów i równoważnych im surowych łańcuchów:

| Zwykły łańcuch | Łańcuch surowy |
| --- | --- |
| "ab*" | r"ab*" |
| "\\ten" | r"\ten" |
| "\\w+\\s+" | r"\w+\s+" | 

## Grupowanie

Nawiasy oprócz zwykłej funkcji, wpływania na kolejność obliczeń, pełnią drugą ważną rolę - tworzą z wyrażenia w nawiasach tzw. grupę.

| Wyrażenie | Znaczenie |
| --- | --- |
|(...) | dopasowanie wyrażenia w nawiasie jako grupy, po dopasowaniu pierwszej grupy można odwoływać się we wzorcu do jej zawartości poprzez odwołanie wsteczne \1 i odpowiednio poprzez \2,\3... do zawartości kolejnych dopasowanych grup |
| (?:...) | nawiasy nieprzechwytujące, od zwykłych nawiasów różnią się tym, że po dopasowaniu nie można odwoływać się do zawartości dopasowanego wyrażenia poprzez odwołania wsteczne |
| (?P<name>...) | tworzy grupę nazwaną name |
| (?P=name) | dopasowuje tekst, który został dopasowany wcześniej przez grupę nazwaną name |
| (?(1)then|else) | wyrażenie warunkowe, jeśli pierwsza grupa przechwytująca dopasowała porcję tekstu, dopasuj wyrażenie then. Jeśli grupa przechwytująca nr 1 nie brała udziału w dopasowaniu tekstu, dopasuj wyrażenie else |

- Po dopasowaniu grupy we wzorcu można odwoływać się we wzorcu do jej zawartości poprzez odwołania wsteczne \numer.
- Numerowanie grup we wzorcu przebiega począwszy od 1, od lewej do prawej, wg. wystąpienia lewego nawiasu otwierającego.
- Cały wzorzec tworzy grupę zerową, do jej zawartości możemy się odwoływać przy zamianie tekstów funkcją sub.
- Dodanie we wzorcu nowej grupy przechwytującej (wyrażenia w nawiasach) może wprowadzić konieczność zmiany numeracji odwołań wstecznych. W celu uniknięcia błędów i większej czytelności wprowadzono także grupy nazwane.

W przypadku użycia grupowania przy zastępowaniu tekstów z użyciem funkcji `sub`:
- w łańcucu zastępującym możemy użyć odwołań wstecznych `\1`, `\2`, ....
- Do grupy zerowej (całe dopasowanie) oraz do grup nazwanych musimy się odwoływać odpowiednio poprzez `\g<0>` oraz `\g<name>`, gdzie `name` to nazwa grupy nazwanej.
- Do grup 1, 2, ... możemy też odwoływać się poprzez \g<1>,\g<2>,.... Jest to przydatne np. do rozróżnienia pomiędzy zawartością grupy dwudziestej `\20` a zawartością grupy drugiej, po której następuje literał 0: `\g<2>0`

Przykłady zastosowania grupowania do wyszukiwania i zastępowania wzorców:

```
pattern = r'\w+ \w+'
r = re.compile(pattern)
m = r.match('Hello world, ...') # dopasowuje pare slow rozdzielonych spacja
```

Dopasowanie pary identycznych słów:
```
pattern = r'(\w+) \1'
r = re.compile(pattern)
m = r.match('Hello world, ...') # brak dopasowania
m = r.match('Hello Hello, ...') # dopasowanie
```

Dopasowanie pary identycznych słów przy pomocy grupy nazwanej:
```
pattern = r'(?P<word>\w+) (?P=word)'  # to samo co r'(\w+) \1' przy pomocy grupy nazwanej
r = re.compile(pattern)
m = r.match('Hello Hello, ...') 
```

Zamiana adresu www na hyperlink:
```
str = r'http://www.python.org'
pattern = r'(http://\w+(\.\w+)+)' 
r = re.compile(pattern)
link = r.sub(r'<a href="\1">\1</a>', str)
```

Zamiana adresu www na hyperlink z użyciem grup nazwanych:
```
str = r'http://www.python.org'
pattern = r'(?P<addr>http://\w+(\.\w+)+)'
r = re.compile(pattern)
link = r.sub(r'<a href="\g<addr>">\g<addr></a>', str)
```

[grouping.py](grouping.py)

## Opcje i modyfikatory

Opcje i modyfikatory wpływają na sposób dopasowywania wzorca w tekście.

| Opcja (długa) | Opcja (krótka) | Znaczenie |
| --- | --- | --- |
| re.IGNORECASE | re.I | Wielkość liter nie jest brana pod uwagę przy dopasowywaniu | 
| re.DOTAL | re.S | Znak . pasuje również do znaku nowej linii |
| re.MULTILINE | re.M | ^ pasuje nie tylko do początku łańcucha, ale także do początku każdej nowej linii w przypadku łańcucha składającego się z wielu linii. W analogiczny sposób modyfikowane jest dopasowanie $ |
| re.VERBOSE | re.X | Możliwość umieszczania komentarzy w wyrażeniu regularnym, spacje nie są częścią wzorca |

Opcje można przekazywać do szeregu funkcji, w tym funkcji `re.compile`. Chcąc przekazać do funkcji wiele opcji należy użyć alternatywy bitowej:
```
r = re.compile("This is regex pattern",  re.VERBOSE | re.IGNORECASE | re.DOTALL | re.MULTILINE)
```

W odróżnieniu od opcji, modyfikatory są częścią samego wzorca.

| Modyfikator| Znaczenie |
| --- | --- |
| (?i) | odpowiednik re.I | 
| (?s) | odpowiednik re.S |
| (?m) | odpowiednik re.M | 
| (?x) | odpowiednik re.X |

- Modyfikatory można łączyć ze sobą. Przykładowo modyfikatory (`?i`) oraz (`?m`) można zapisać łącznie jako (`?im`).
- Włączona modyfikatorem opcja dotyczy całego wzorca w którym się znajduje, niezależnie od położenia.
- W Pythonie opcje można włączać, ale nie można ich wyłączać modyfikatorem, tzn. nie są zaimplementowane wyłączniki typu (`?-i`).

Poniżej mamy trzy równoważne sposoby użycia tego samego wzorca bez oraz z użyciem komentarzy:
```
a = re.compile(r"\d+\.\d*")

b = re.compile(r"""\d+   # czesc calkowita
                   \.    # kropka dziesietna
                   \d*   # czesc ulamkowa""", re.X)

c = re.compile(r"""(?x)  # wlacz komentarze
                   \d+   # czesc calkowita
                   \.    # kropka dziesietna
                   \d*   # czesc ulamkowa""")
```

Dodatkowo istnieje jeszcze możliwość wstawiania we wzorcu komentarzy w postaci (`?#komentarz`).


## Moduł `re`
Wyrażenia regularne w Pythonie zaimplementowane są w module `re`. Moduł ten pozwala na dopasowywanie oraz zastępownie fragmentów tekstów przy pomocy opisanej powyżej składni.

Poniższy przykład znajduje w łańcuchu liczbę zmiennoprzecinkową przy pomocy prostej wersji wyrażenia regularnego dla liczb zmiennoprzecinkowych.

```
import re

pattern = r'(\d+).(\d*)'
str = '342.79+12.56'

m = re.match(pattern,str)
if m:
    print("{0} pasuje do {1}".format(pattern, str) )
else:
    print("{0} nie pasuje do {1}".format(pattern, str) )
```

[simple.py](simple.py)

W przypadku, gdy będziemy wyszukiwali dany wzorzec wiele razy, efektywniej jest na początku dokonać kompilacji wzorca do obiektu. Obiekty wyrażeń regularnych tworzone są metodą re.compile Poprzedni przykład, tym razem z kompilacją wzorca będzie wyglądał następująco:

```
import re

pattern = r'(\d+).(\d*)'
str = '342.79+12.56'

r = re.compile(pattern)
m = r.match(str)
if m:
    print("{0} pasuje do {1}".format(pattern, str) )
else:
    print("{0} nie pasuje do {1}".format(pattern, str) )
```

Poprzedni przykład z kompilacją wzorca: [simple_compile.py](simple_compile.py)

Analogicznie do metody match w powyższych przykładach, większość metod modułu re istnieje w dwóch wariantach: z kompilacją wzorca i bez kompilacji wzorca.


## Obiekty dopasowania

W przypadku dopasowania zwracany jest tzw. obiekt dopasowania (ang. _match object_). Obiekty dopasowania posiadają m.in. następujące metody:
- `group(n)` - zwraca tekst dopasowania dla grupy _n_,
- `groups()` - zwraca krotkę zawierającą dopasowania wszystkich grup, począwszy od 1. grupy,
- `start(n)` - zwraca indeks początkowy dla grupy _n_,
- `end(n)` - zwraca indeks końcowy dla grupy _n_,
- `span(n)` - zwraca dla grupy _n_ krotkę (indeks początkowy, indeks końcowy).

Najważniejsza z powyższych jest funkcja `group`. Dla grupy 0 funkcja zwraca całe dopasowane wyrażenie regularne. Dla grup 1,2,... funkcja zwraca dopasowania w kolejnych nawiasach (nawiasy nieprzechwytujące nie są brane pod uwagę).

```
import re

pattern = r'(\d+).(\d*)'
str = '342.79+12.56'

r = re.compile(pattern)
m = r.match(str)

print( m.group(0) )           # 342.79, cale dopasowanie
print( m.group(1) )           # 342, dopasowanie (\d+)
print( m.group(2) )           # 79, dopasowanie (\d*)
print( m.start(1), m.end(1) ) # 0, 3
print( m.start(2), m.end(2) ) # 4, 6
```

[match.py](match.py)

## Metody modułu `re`

Najważniejsze metody modułu `re` przedstawia poniższa tabela.

| Metoda | Opis |
| --- | --- |
| `re.search(pattern, str [, pos [, endpos]])` | Szuka dopasowania wyrażenia regularnego pattern w całym łańcuchu str. Zakres poszukiwań można ograniczyć podając parametry pos (indeks łańcucha, gdzie rozpocznie się poszukiwanie) oraz endpos, (indeks łańcucha, gdzie skończy się poszukiwanie). |
| `re.match(pattern, str [, pos [, endpos]]`) |  Szuka dopasowania wyrażenia regularnego pattern, ale tylko na początku łańcucha str, czym różni się od funkcji search | 
| `re.split(pattern, str)` | Zwraca listę stringów powstałą z podzielenia łańcucha str na każdym dopasowania wyrażenia regularnego pattern. Jeśli wzorzec pattern umieszczono w nawiasach, każde dopasowanie tego wzorca na łańcuchu str znajdzie się w liście wynikowej. |
`re.findall(pattern, str)` | Jeśli wzorzec nie zawiera nawiasów przechwytujących znajduje wszystkie dopasowania wyrażenia regularnego pattern w łańcuchu str i zwraca je w formie listy stringów. Jeśli wzorzec pattern zawiera nawiasy przechwytujące, zwraca dopasowania grup przechwytujących w formie listy krotek. W odróżnieniu od funkcji findall funkcje search oraz match znajdują tylko jedno dopasowanie. |
`re.finditer(pattern, str)` | Zwraca iterator zwracający kolejne obiekty dopasowania wzorca pattern w łańcuchu str. |
`re.sub(pattern, repl, str)` | Zwraca kopię łańcucha str, gdzie wszystkie dopasowania wyrażenia regularnego pattern zamienione zostały na repl. |
`re.subn(pattern, repl, str)` | Działa podobnie jak funkcja sub, zwraca parę (zmodyfikowany łańcuch, liczba zamian) |

Analogiczne metody istnieją dla obiektów wyrażeń regularnych, powstałych w wyniku kompilacji wzorca. Metody te nie przyjmują pierwszego parametru `pattern`, gdyż są wywoływane dla skompilowanego obiektu wzorca.

## Przykłady
Poniżej znajdują się przykłady użycia wyżej opisanych funkcji.  
[funcs.py](funcs.py)

## Materiały
- [Szczegółowa dokumentacja modułu re](http://docs.python.org/2/library/re.html)
- http://www.regular-expressions.info
- Regular Expressions Cookbook, J. Goyvaerts, S. Levithan