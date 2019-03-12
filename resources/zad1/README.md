## Lab 1

Zadanie polega na stworzeniu analizatora leksykalnego (skanera) dla prostego języka umożliwiającego obliczenia na macierzach. Analizator leksykalny powinien rozpoznawać następujące leksemy:

*   operatory binare: +, -, *, /
*   macierzowe operatory binarne (dla operacji element po elemencie): .+, .-, .*, ./
*   operatory przypisania: =, +=, -=, *=, /=
*   operatory relacyjne: <, >, <=, >=, !=, ==
*   nawiasy: (,), [,], {,}
*   operator zakresu: :
*   transpozycja macierzy: '
*   przecinek i średnik: , ;
*   słowa kluczowe: `if`, `else`, `for`, `while`
*   słowa kluczowe: `break`, `continue` oraz `return`
*   słowa kluczowe: `eye`, `zeros` oraz `ones`
*   słowa kluczowe: `print`
*   identyfikatory (pierwszy znak identyfikatora to litera lub znak _, w kolejnych znakach mogą dodatkowo wystąpić cyfry)
*   liczby całkowite
*   liczby zmiennoprzecinkowe
*   stringi

Dla rozpoznanych leksemów stworzony skaner powinien zwracać:

*   odpowiadający token
*   rozpoznany leksem
*   numer linii
*   opcjonalnie może być zwracany numer kolumny

Następujące znaki powinny być pomijane:

*   białe znaki: spacje, tabulatory, znaki nowej linii
*   komentarze: komentarze rozpoczynające się znakiem # do znaku końca linii

Przykład.  
Dla następującego [kodu](example.txt):

```
A = zeros(5); # create 5x5 matrix filled with zeros
B = ones(7);  # create 7x7 matrix filled with ones
I = eye(10);  # create 10x10 matrix filled with ones on diagonal and zeros elsewhere
D1 = A.+B' ;  # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B
```

analizator leksykalny powinien zwracać następującą sekwencję i wypisywać ją na standardowym wyjściu:

```
(1,1): ID(A)
(1,3): =(=)
(1,5): ZEROS(zeros)
(1,10): ((()
(1,11): INTNUM(5)
(1,12): )())
(1,13): ;(;)
(2,1): ID(B)
(2,3): =(=)
(2,5): ONES(ones)
(2,9): ((()
(2,10): INTNUM(7)
(2,11): )())
(2,12): ;(;)
(3,1): ID(I)
(3,3): =(=)
(3,5): EYE(eye)
(3,8): ((()
(3,9): INTNUM(10)
(3,11): )())
(3,12): ;(;)
(4,1): ID(D1)
(4,4): =(=)
(4,6): ID(A)
(4,7): DOTADD(.+)
(4,9): ID(B)
(4,10): '(')
(4,12): ;(;)
(5,1): ID(D2)
(5,4): SUBASSIGN(-=)
(5,7): ID(A)
(5,8): DOTSUB(.-)
(5,10): ID(B)
(5,11): '(')
(5,13): ;(;)
(6,1): ID(D3)
(6,4): MULASSIGN(*=)
(6,7): ID(A)
(6,8): DOTMUL(.*)
(6,10): ID(B)
(6,11): '(')
(6,13): ;(;)
(7,1): ID(D4)
(7,4): DIVASSIGN(/=)
(7,7): ID(A)
(7,8): DOTDIV(./)
(7,10): ID(B)
(7,11): '(')
(7,13): ;(;)
```

- Do rozwiązania zadania należy użyć generatora skanerów, np. generatora `PLY`.
- Skaner powinien rozpoznawać niepoprawne leksykalnie wejście. W takim przypadku powinien zostać wypisany numer niepoprawnej linii wraz z szczegółową informacją o błędzie.
- Do stworzenia skanera można wykorzystać plik [main.py](main.py) lub [main_oo.py](main_oo.py) (należy stworzyć odpowiednio skaner "strukturalny" scanner.py lub obiektowy scanner_oo.py).
*   Przykładowe wejście [example_full.txt](example_full.txt)
