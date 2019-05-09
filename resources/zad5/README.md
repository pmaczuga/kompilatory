## Lab 5
Zadanie jest kontynuacją poprzedniego zadania.

Zadanie polega na stworzeniu interpretera języka wyspecyfikowanego w poprzednich zajęciach. Interpretacja powinna być wykonywana tylko wtedy, gdy poprzednie etapy zakończyły się sukcesem -- nie wystąpiły żadne błędy syntaktyczne lub semantyczne.

### Implementacja
Do implementacji zadania należy wykorzystać wzorzec visitor. Tym razem nie będziemy używać implementacji z poprzednich zajęć (dla każdej klasy z AST definicja funkcji `vistit_<classname>` w odpowiednim wizytorze), lecz należy użyć implementacji opartej na dekoratorach. W tym celu w wizytorze Interpreter należy dla każdej klasy z AST zdefiniować metodę visit, dekorowaną nazwą tej klasy.

### Pamięć interpretera
Poza trywialnym przypadkiem jednego, globalnego zakresu, bieżące wartości zmiennych nie mogą być przechowywane w tablicy symboli. W pozostałych przypadkach potrzebna jest osobna pamięć interpretera o strukturze stosu.
Pamięć globalna `globalMemory` służy do przechowywania wartości zmiennych w zakresie globalnym i jego zakresach potomnych niefunkcyjnych. Pamięć ta możę zostać zaimplementowana jako instacja klasy `MemoryStack`.

### Przekazywanie sterowania
Do zaimplementowania przekazywania sterowania z instrukcji `break`, `continue` nie wystarczy użycie zwykłej instrukcji `return`, gdyż wspomniane instrukcje mogą być zagnieżdzone dowolnie głęboko w pętli. Zamiast tego należy posłużyć się mechanizmem wyjątków: zgłaszanie wyjątku przy interpretacji instrukcji `break` lub `continue` oraz jego przechwytywanie w funkcjach visit interpretujących pętle (oraz w funkcji visit interpretującej wywołanie funkcji, jeśli język umożliwia definiowanie i wywoływanie funkcji).

Do stworzenia interpretera można wykorzystać pliki:

[visit.py](visit.py) [Imlementation of visitor pattern of Curtis Schlak]  
[Interpreter.py](Interpreter.py)  
[Memory.py](Interpreter.py)  
[Exceptions.py](Interpreter.py)  
[main.py](Interpreter.py)  
