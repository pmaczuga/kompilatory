# Parser PLY

## Instalacja
Do instalacji pakietu PLY można wykorzystać menadżera pakietów. Szczegóły zależą od konkretnego systemu operacyjnego.
- Windows: należy użyć Python Package Managera (`pypm`): `pypm install PLY`
- Linux (Debian): `apt-get: apt-get install python-ply`

Alternatywnie można pobrać pakiet [tutaj](http://www.dabeaz.com/ply/ply-3.4.tar.gz), a następnie po rozpakowaniu go zainstalować komendą:

```
C:\...\ply-3.4> python setup.py install
```

W przypadku braku uprawnień do zapisu do odpowiednich katalogów wystarczy rozpakować pobrany plik w katalogu roboczym.

## Wprowadzenie

Generator parserów PLY (Python-Lex-Yacc) jest odpowiednikiem narzędzi `bison/flex` dla języka Python, generującym parsery typu LALR (domyślnie) lub SLR. PLY składa się z dwóch modułów: `lex` (analiza leksykalna) oraz `yacc` (parsing). W odróżnieniu od odpowiedników `bison/flex` dla języka C:
- Specyfikacja gramatyki jest zawarta bezpośrednio w pliku źródłowym analizatora.
- PLY narzuca pewne konwencje nazewnicze oraz wykorzystuje mechanizm introspekcji, dzięki czemu generacja parsera oraz jego wykonanie odbywa się w jednej fazie.
- Nie jest potrzebny osobny język specyfikacji jak w przypadku bisona/flexa. Do specyfikację gramatyki wykorzystuję się docstring funkcji.

## Analizator leksykalny

Przed rozpoczęciem pracy zaimportujemy analizator leksykalny:
```
import ply.lex as lex;
```

Na początku zdefiniujemy listę leksemów rozpoznawanych przez analizator. Służy do tego zmienna `tokens`:
```
tokens = (  'PLUS',  'MINUS',  'TIMES',  'DIVIDE',  'LPAREN',  'RPAREN' ,  'NUMBER', 'ID' )
```

Z każdym leksem należy powiązać odpowiednie wyrażenie regularne. W tym celu dla każdego leksemu definiujemy zmienną o tej samej nazwie poprzedzoną przedrostkiem t_. Jako wyrażeń regularnych używa się najczęściej tzw. surowych łańcuchów (`raw strings`), co pozwala uniknąć kłopotów z cytowaniem znaków ukośnika \ :
```
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
```

Dla stałych leksemów jednoznakowych definiowanie odrębnej nazwy leksemu może wydawać się nadmiarowe i zaciemniać kod. Takie leksemy, do których chcemy odwoływać się poprzez ich wartość znakową, należy umieścić na liście `literals`:
```
literals = [ '+','-','*','/','(',')' ]
lub alternatywnie jako łańcuch znakowy:
literals = "+-*/()"
```

W przypadku leksemów takich jak `NUMBER` lub `ID` chcemy dodatkowo przekazać wartość związaną z danym tokenem (liczbę dla tokenu `NUMBER`, nazwę identyfikatora dla tokenu ID). Dla takich leksemów definiujemy funkcję zamiast zwykłej zmiennej. `Docstring `funkcji zawiera wyrażenie regularne opisujące dopasowywany token:
```
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t
```

Aby usunąć wybrane znaki ze strumienia wejściowego (np. spacje i tabulacje) definiujemy zmienną `t_ignore`:
```
t_ignore = '  \t'
```

Analizator nie posiada wbudowanej obsługi numerów linii. Musimy sami dostarczyć odpowiednią funkcję.
```
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
```

Powyższa funkcja pomija znaki nowi linii oraz dodatkowo zapamiętuje numer linii przetwarzanej obecnie przez analizator:

W sytuacji, gdy analizator leksykalny napotka na znak, którego nie może rozpoznać, możemy zasygnalizować błąd. Służy do tego funkcja `t_error`:
```
def t_error(t) :
    print "Illegal character '%s'" %t.value[0]
    t.lexer.skip(1)
```

Pozostaje tylko konstrukcja analizatora:
```
lexer = lex.lex()
fh = open(sys.argv[1], "r");
lexer.input( fh.read() )
for token in lexer:
    print("line %d: %s(%s)" %(token.lineno, token.type, token.value))
```

Źródła: [simple_lex.py](simple_lex.py)

##Stany leksera

Analogicznie do flexa, w analizatorze ply.lex można zadeklarować stany wyłączne (ang. _exclusive_) lub niewyłączne (ang. _inclusive_). Służy do tego zmienna `states`:
```
states = (
    ('foo','exclusive'),
    ('bar','inclusive'),
)
```

Zadeklarowaliśmy dwa stany: `foo` (wyłączny) oraz `bar` (niewyłączny). Zdefiniowane stany możemy wykorzystać przy tworzeniu leksemów:
```
t_foo_NUMBER = r'\d+'                      # Token 'NUMBER' in state 'foo'        
t_bar_ID     = r'[a-zA-Z_][a-zA-Z0-9_]*'   # Token 'ID' in state 'bar'

def t_foo_newline(t):
    r'\n'
    t.lexer.lineno += 1
```

Leksem `NUMBER` zostanie dopasowany tylko, gdy analizator znajduje się w stanie `foo`, podobnie leksem `ID` zostanie dopasowany tylko w stanie `bar`. Analogiczne zasady obowiązują dla funkcji. 

Token może być dopasowywany w jednym z kilku stanów analizatora. Przykładowo:
```
t_foo_bar_NUMBER = r'\d+'         # Defines token 'NUMBER' in both state 'foo' and 'bar'
```

Token, który ma być dopasowywany w dowolnym stanie analizatora definiujemy następująco:
```
t_ANY_NUMBER = r'\d+'         # Defines a token 'NUMBER' in all states
```

W większości przypadków nie specyfikuje się stanu w deklaracji tokenu. Przyjmuje się wtedy, że token związany jest ze stanem początkowym analizatora `INITIAL`. Tak więc dwie poniższe deklaracje są równoważne:
```
t_NUMBER = r'\d+'
t_INITIAL_NUMBER = r'\d+'
```

Do zmiany stanu analizatora w czasie analizy leksykalnej lub parsingu służy funkcja `begin()`:
```
def t_begin_foo(t):
    r'start_foo'
    t.lexer.begin('foo')             # Starts 'foo' state

def t_foo_end(t):
    r'end_foo'
    t.lexer.begin('INITIAL')        # Back to the initial state
```

Do zmiany stanu analizatora można też posłużyć się stosem oraz funkcjami `push_state()` i `pop_state()`: 

Źródła: [comments.py](comments.py)

## Priorytety operatorów

PLY umożliwia definiowanie priorytetów operatorów. Do określania priorytetów operatorów służy zmienna `precedence`. Razem z priorytetem należy określić łączność operatorów. Do wyboru mamy następujące możliwości:
- `left` - łączność lewostronna,
- `right` - łączność prawostronna,
- `nonassoc` - operator binarny, brak łączności.

Przykładowo definicja priorytetów operatorów dla gramatyki prostych wyrażeń arytmetycznych będzie wyglądała następująco:
```
precedence = (
    ("left", '+', '-'),
    ("left", '*', '/')   )
```

Wynika z niej, że operatory dodawania i dodawanie mają niższy priorytet (jako wcześniejsze na liście) od operatorów mnożenia i dzielenia oraz, że wszystkie powyższe operatory są lewostronnie łączne.


## Analiza syntaktyczna
Rozważmy gramatykę prostych wyrażeń arytmetycznych:
```
expression -> expression ADD_OP expression
           |  expression MUL_OP expression
           |  '('  expression ')'
           |  NUMBER
```

Na początku należy zaimportować parser:
```
import ply.yacc as yacc
```

Reguły gramatyki reprezentowane są przez funkcje, których nazwa musi rozpoczynać się przedrostkiem `p_`. Same reguły gramatyki zapisane są w _docstringu_ funkcji. Nazwa funkcji występująca po przedrostku `p_` nie jest istotna z punktu widzenia samego parsingu, ale oczywiście warto nadawać nazwy oddające znaczenie funkcji. Wartości symboli w regule (produkcji) gramatyki dostępne są poprzez parametr `p`: `p[0]` oznacza wartość lewej strony produkcji, `p[1]` wartość pierwszego symbolu po prawej stronie produkcji, itd.  

Przykładowa funkcja obsługująca działania binarne będzie wyglądała następująco:
```
def p_expression_binop(p):
"""expression  : expression ADD_OP expression
               | expression MUL_OP expression"""
    if p[2] == '+'   : p[0] = p[1] + p[3]
    elif p[2] == '-' : p[0] = p[1] - p[3]               
    elif p[2] == '*' : p[0] = p[1] * p[3]                         
    elif p[2] == '/' : p[0] = p[1] / p[3] 
```

    
## Łączenie reguł
Całą gramatykę możnaby umieścić w _docstringu_ jednej funkcji, w tym produkcje rozpoczynające się różnymi symbolami, a właściwą produkcję wybierać na podstawie coraz bardziej skomplikowanych instrukcji warunkowych. W ten sposób powtarzalibyśmy pracę, którą wykonał parser. Dlatego z każdą funkcją najlepiej zwiaząć jedną lub co najwyżej kilka produkcji.


## Obsługa błędów
Analogicznie do leksera dostępna jest funkcja obsługująca błędy parsingu, o nazwie `p_error`:
```
def p_error(p):
    print(  "syntax error in line %d" % p.lineno)
```

Dostępny jest też specjalny token `error`, którego można używać w produkcjach, analogicznie jak w bisonie. 
Można również samemu zasygnalizować błąd, zgłaszając w regule wyjątek: `raise SyntaxError`:
```
def p_production(p):
    'production : some production ...'
    raise SyntaxError
```

W tym wypadku nie jest wywoływana funkcja p_error.


## Prosty kalkulator
Zozstała nam tylko konstrukcja parsera oraz powiązanego z nim analizatora leksykalnego:
```
lexer = lex.lex()
parser = yacc.yacc()
text = file.read()
parser.parse(text, lexer=lexer)
```

Źródła: [simple_expressions.py](simple_expressions.py)

Kolejny przykład umożliwia definiowanie zmiennych całkowitych i wykorzystywanie ich w wyrażeniach arytmetycznych. W tym celu tworzona jest tablica symboli (w postaci słownika) przechowująca wartości używanych zmiennych. 

Źródła: [simple_calculator.py](simple_calculator.py)


## Dokumentacja parsera PLY
Pełna dokumentacja dotycząca parsera PLY znajduje się [tutaj](http://www.dabeaz.com/ply/ply.html).