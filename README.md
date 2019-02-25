# Kompilatory

Homepage:  
http://home.agh.edu.pl/~mkuta/tklab/

<div class="WordSection1">

<span lang="PL" style="font-size:18.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Procesy - materiały pomocnicze</span>

**<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Proces</span>**<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">jest pojedynczą instancją wykonującego się programu.</span> <span style="font-size:
11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Możemy w nim wyróżnić:</span>

*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">segment kodu</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif"> - zawiera kod binarny aktualnie wykonywanego programu. Znajduje się w nim kod zaimplementowanych przez nas funkcji oraz funkcji dołączanych z bibliotek. Zapisane w tym segmencie adresy funkcji pozwalają na ich lokalizację.</span>
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">segment danych</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif"> - zawiera zainicjalizowane zmienne globalne zdefiniowane w programie. Adres segmentu danych można ustalić na podstawie adresu zmiennej globalnej.</span>
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">segment BSS - _Block Started by Symbol_</span>**<span style="font-size:
         11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif"> - zawiera niezainicjalizowane zmienne globalne</span>
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">segment stosu</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif"> - zmienne lokalne oraz adresy powrotu wykorzystywane podczas powrotu z wykonywanej funkcji. Ponieważ proces moze pracować w trybie użytkownika lub trybie jądra, każdy z tych trybów ma do dyspozycji oddzielny stos.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Każdemu procesowi przydzielane są zasoby czas procesora, pamięć, dostęp do urządeń we/wy oraz plików etc). Część tych zasobów jest do wyłącznej dyspozycji procesu, zaś część jest współdzielona z innymi procesami.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Na proces nakładane są pewne ograniczenia dotyczące zasobów systemowych,   
możemy do nich uzyskać dostęp następującymi funkcjami z </span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">sys/resource.h:</span>**

**<span style="font-size:11.5pt;font-family:&quot;Trebuchet MS&quot;,sans-serif;color:red">int getrlimit (int resource, struct rlimit *rlptr) Resource to jedno z makr określające rodzaj zasobu</span>**

**<span style="font-size:11.5pt;font-family:&quot;Trebuchet MS&quot;,sans-serif;color:red">int setrlimit (int resource, const struct rlimit *rlptr)</span>**

**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">struct rlimit {</span>**

**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">        rlim_t rlim_cur; //bieżące ograniczenie</span>**

**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">        rlim_t rlim_max; //maksymalne ograniczenie</span>**

**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">}</span>**

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> **Identyfikatory procesów**</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Każdy proces w systemie UNIX ma przypisany unikalny identyfikator - **PID**. Jest to 16-bitowa, nieujemna liczba całkowita przypisywana do każdego procesu podczas jego tworzenia. Niektóre identyfikatory są odgórnie zarezerwowane dla specjalnych procesów w systemie, (swapper – 0, _init -1 etc)_.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">System UNIX pamięta także identyfikator procesu macierzystego - ta informacja jest zapisywana jako **PPID** (Parent PID).</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> Do każdego procesu przypisane są również (rzeczywiste) identyfikatory użytkownika (**UID**) oraz grupy (**GID**), określające kto dany proces utworzył. Istnieją również efektywne UID i GID przechowujące informacje o identyfikatorze właściciela oraz grupy właściciela programu.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Do pobrania informacji o identyfikatorach procesu możemy posłużyć się funkcjami z biblioteki unistd.h, takimi jak:</span>

*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">pid_t getpid(void) - zwraca PID procesu wywołującego funkcję</span>**
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">pid_t getppid(void) - zwraca PID procesu macierzystego</span>**
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">uid_t getuid(void) - zwraca rzeczywisty identyfikator użytkownika UID</span>**
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">uid_t geteuid(void) - zwraca efektywny identyfikator użytkownika UID</span>**
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">gid_t getgid(void) - zwraca rzeczywisty identyfikator grupy GID</span>**
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">gid_t getegid(void) - zwraca efektywny identyfikator grupy GID</span>**

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Definicje niezbędnych typów znajdziemy w </span>**<span style="font-size:11.5pt;
font-family:&quot;Segoe UI&quot;,sans-serif;color:red">sys/types.h.</span>**

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> </span>

<span style="font-size:18.0pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Tworzenie procesów</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">W systemie Unix każdy proces, za wyjątkiem procesu o numerze 0 jest tworzony przez wykonanie przez inny proces funkcji _fork_. Proces ją wykonujący nazywa się **procesem macierzystym**, zaś nowoutworzony - **procesem potomnym**. Procesy, podobnie jak katalogi, tworzą drzewiastą strukturę hierarchiczną - każdy proces w systemie ma jeden proces macierzysty, lecz może mieć wiele procesów potomnych. Korzeniem takiego drzewa w systemie UNIX jest proces o PID równym 1, czyli _init_.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Mechanizm tworzenia procesu w systemach unixowych przedstawiono poniżej:</span>

<span style="font-size:18.0pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Funkcje systemowe</span>

<span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Funkcje _fork_ oraz _vfork_</span>

<span style="font-size:10.0pt;font-family:Consolas;
color:#212529">·     </span><span style="font-size:
10.0pt;font-family:Consolas;color:red">    **pid_t fork( void )**</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">W momencie jej wywołania tworzony jest nowy proces, będący potomnym dla tego, w którym właśnie została wywołana funkcja _fork_. Jest on kopią procesu macierzystego - otrzymuje duplikat obszaru danych, sterty i stosu (a więc nie współdzieli danych). Funkcja _fork_ jest wywoływana raz, lecz zwraca wartość dwukrotnie - proces potomny otrzymuje wartość 0, a proces macierzysty PID nowego procesu. Jest to konieczne nie tylko ze względu na możliwość rozróżnienia procesów w kodzie programu: proces macierzysty musi otrzymać PID nowego potomka, ponieważ nie istnieje żadna funkcja umożliwiająca wylistowanie wszystkich procesów potomnych. W przypadku procesu potomnego nie jest konieczne podawanie PID jego procesu macierzystego, ponieważ ten jest określony jednoznacznie (i można go wydobyć np. za pomocą funkcji getppid). Z kolei 0 jest bezpieczną wartością, ponieważ jest zarezerwowana dla procesu demona wymiany i nie ma możliwości utworzenia nowego procesu o takim PID.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Po wywołaniu forka oba procesy (macierzysty i potomny) kontynuują swoje działanie (od linii następnej po wywołaniu forka czyli efektem kodu:</span>

<span style="font-size:10.0pt;font-family:Consolas;
color:red">  **#include <stdio.h>**</span>

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">   main(){</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">               printf("Poczatek\n");</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">               fork();</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">               printf("Koniec\n");</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">}</span>**

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Będzie:</span>

_<span style="font-size:10.0pt;font-family:Consolas;
color:#212529">Poczatek  //z macierzystego przed wywołaniem forka</span>_

_<span style="font-size:10.0pt;font-family:Consolas;
color:#212529">Koniec  // z macierzystego lub potomnego po forku</span>_

_<span style="font-size:10.0pt;font-family:Consolas;
color:#212529">Koniec  //z macierzystego lub potmnego po forku</span>_

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> </span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Powyższy komentarz _// z macierzystego lub potomnego po forku wynika z faktu _że nie można przewidzieć, który z procesów będzie wykonywać swoje instrukcje jako pierwszy, dlatego w przypadku gdy wymaga się od nich współpracy, należy zastosować jakieś metody synchronizacji komunikacji międzyprocesowej.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">vfork</span>

*   <span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C"> </span>**<span style="font-size:7.5pt;font-family:&quot;inherit&quot;,serif;color:red">pid_t vfork( void ) </span>**

<span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Funkcji tej używa się w przypadku gdy głównym zadaniem nowego procesu jest wywołanie funkcji </span>_<span style="font-size:7.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">exec</span>_<span style="font-size:7.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">. _vfork_ „odblokuje” proces macierzysty dopiero w momencie wywołania funkcji _exec_ lub _exit_. Inną ważną cechą tej funkcji jest współdzielenie przestrzeni adresowej przez obydwa procesy.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Identyfikacja procesu macierzystego i potomnego</span>

<span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">#include <stdio.h></span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   #include <sys/types.h></span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   #include <unistd.h></span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  

</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   int main() {</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      pid_t child_pid;</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      printf("PID glownego programu: %d\n", (int)getpid());</span><span style="font-size:
13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      child_pid = fork();</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      if(child_pid!=0) {</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">         printf("Proces rodzica: Proces rodzica ma pid:%d\n", (int)getpid());</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">         printf("Proces rodzica: Proces dziecka ma pid:%d\n", (int)child_pid);</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      } else {</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">         printf("Proces dziecka: Proces rodzica ma pid:%d\n",(int)getppid());</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">         printf("Proces dziecka: Proces dziecka ma pid:%d\n",(int)getpid());</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      }</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  

</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">      return 0;</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   }</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">  

Przykładowy wynik dział</span><span style="font-size:13.5pt;font-family:&quot;Times New Roman&quot;,serif;
color:#373A3C">‚</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">ania programu:  

</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   PID glownego programu: 2359</span><span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;
color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   Proces rodzica: Proces rodzica ma pid:2359</span><span style="font-size:13.5pt;
font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   Proces rodzica: Proces dziecka ma pid:2360</span><span style="font-size:13.5pt;
font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   Proces dziecka: Proces rodzica ma pid:2359</span><span style="font-size:13.5pt;
font-family:&quot;inherit&quot;,serif;color:#373A3C">  
</span><span style="font-size:17.0pt;font-family:Consolas;color:#E83E8C">   Proces dziecka: Proces dziecka ma pid:2360</span>

<span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C"> </span>

<span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Funkcje rodziny _exec_</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Funkcje z rodziny _exec służą do uruchomienia w ramach procesu innego programu_.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">W wyniku wywołania funkcji typu **exec **następuje reinicjalizacja segmentów kodu, danych i stosu procesu ale nie zmieniają się takie atrybuty procesu jak pid, ppid, tablica otwartych plików i kilka innych atrybutów z segmentu danych systemowych</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> </span>

*   **<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">int execl(char const *path, char const *arg0, ...)</span>****<span style="font-size:
         11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red"> </span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">  
    funkcja jako pierwszy argument przyjmuje ścieżkę do pliku, następne są argumenty wywołania funkcji, gdzie arg0 jest nazwą programu</span>
*   **<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">int execle(char const *path, char const *arg0, ..., char const * const *envp)</span>****<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red"> </span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">  
    podobnie jak execl, ale pozwala na podanie w ostatnim argumencie tablicy ze zmiennymi środowiskowymi</span>
*   **<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">int execlp(char const *file, char const *arg0, ...)</span>****<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red"> </span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">  
    również przyjmuje listę argumentów ale, nie podajemy tutaj ścieżki do pliku, lecz samą jego nazwę, zmienna środowiskowa PATH zostanie przeszukana w celu zlokalizowania pliku</span>
*   **<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">int execv(char const *path, char const * const * argv)</span>****<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red"> </span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">  
    analogicznie do execl, ale argumenty podawane są w tablicy</span>
*   **<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">int execve(char const *path, char const * const *argv, char const * const *envp)</span>****<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
         color:red"> </span>**<span style="font-size:11.5pt;font-family:
         &quot;Segoe UI&quot;,sans-serif">  
    analogicznie do execle, również argumenty przekazujemy tutaj w tablicy tablic znakowych</span>
*   **<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">int execvp(char const *file, char const * const *argv)</span>****<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red"> </span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">  
    analogicznie do execlp, argumenty w tablicy</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Różnice pomiędzy wywołaniami funkcji **exec **wynikają głównie z różnego sposobu budowy ich listy argumentów: w przypadku funkcji **execl **i **execlp **są one podane w postaci listy, a w przypadku funkcji **execv **i **execvp **jako tablica. </span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Zarówno lista argumentów, jak i tablica wskaźników musi być zakończona wartością NULL. Funkcja **execle **dodatkowo ustala środowisko wykonywanego procesu.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Funkcje **execlp **oraz **execvp **szukają pliku wykonywalnego na podstawie ścieżki przeszukiwania podanej w zmiennej środowiskowej PATH. Jeśli zmienna ta nie istnieje, przyjmowana jest domyślna ścieżka :/bin:/usr/bin.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> </span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Wartością zwrotną funkcji typu **exec **jest _status_, przy czym jest ona zwracana tylko wtedy, gdy funkcja</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">zakończy się niepoprawnie, będzie to zatem wartość -1.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">PRZYKŁADY</span>

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">execl(„/bin/ls", „ls", „-l",null)</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">execlp(„ls", „ls", „-l",null)</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">char* const av[]={„ls", „-l", null}</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">execv(„/bin/ls", av)</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">char* const av[]={„ls", „-l", null}</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">execvp(„ls", av)</span>**

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Funkcje _exec_ **nie tworzą nowego procesu**, tak jak w przypadku funkcji _fork_. Należy pamiętać, że jeśli w programie wywołamy funkcję _exec_, to kod znajdujący się dalej w programie nie zostanie wykonany, chyba że wystąpi błąd.</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Przykład połączenia funkcji fork i exec</span>

**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">main.c:</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  

</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   #include <stdio.h></span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   #include <sys/types.h></span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  

</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   int main() {</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      pid_t child_pid;</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      child_pid = fork();</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      if(child_pid!=0) {</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">         printf("Ten napis zostal wyswietlony w programie 'main'!\n");</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      } else {</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">         execvp("./child", NULL);</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      }</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  

</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      return 0;</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   }</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  

</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">child.c:</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  

</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   #include <stdio.h></span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  

</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   int main() {</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      printf("Ten napis zostal wyswietlony przez program 'child'!\n");</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">      return 0;</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">  
</span>**<span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   }</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  

Wynikiem działania programu jest:  

</span><span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   Ten napis zostal wyswietlony w programie 'main'!</span><span style="font-size:11.5pt;
font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">  
</span><span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">   </span><span lang="PL" style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">Ten napis zostal wyswietlony przez program 'child'!</span>

<span lang="PL" style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Funkcje _wait_ oraz _waitpid_</span>

<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Proces macierzysty może się dowiedzieć o sposobie zakończenia bezpośredniego potomka przez wywołanie funkcji systemowej _wait_. Jeśli wywołanie funkcji _wait_ nastąpi przed zakończeniem potomka, przodek zostaje zawieszony w oczekiwaniu na to zakończenie. Jeżeli proces macierzysty zakończy działanie przed procesem potomnym, to proces potomny nazywany jest sierotą (ang. orphant) i jest „adoptowany" przez proces systemowy _init_, który staję się w ten sposób jego przodkiem. Jeżeli proces potomny zakończył działanie przed wywołaniem funkcji _wait_ w procesie macierzystym, potomek pozostanie w stanie _zombi_. Zombi jest procesem, który zwalnia wszystkie zasoby (nie zajmuje pamięci, nie jest mu przydzielany procesor), zajmuje jedynie miejsce w tablicy procesów w jądrze systemu operacyjnego i zwalnia je dopiero w momencie wywołania funkcji _wait_ przez proces macierzysty, lub w momencie zakończenia procesu macierzystego.</span>

<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Aby pobrać stan zakończenia procesu potomnego należy użyć jednej z dwóch funkcji (plik nagłówkowy </span><span lang="PL" style="font-size:10.0pt;font-family:
Consolas;color:#E83E8C">sys/wait.h</span><span lang="PL" style="font-size:11.5pt;
font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">):</span>

<span style="font-size:10.0pt;font-family:Consolas;
color:#212529">·        </span>** <span style="font-size:10.0pt;font-family:Consolas;color:red">pid_t wait ( int *statloc )</span>**

<span style="font-size:10.0pt;font-family:Consolas;
color:#212529">·        </span>** <span style="font-size:10.0pt;font-family:Consolas;color:red">pid_t waitpid( pid_t pid, int *statloc, int options )</span>**

<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Wywołując _wait_ lub _waitpid_ proces może:</span>

*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">ulec zablokowaniu (jeśli wszystkie procesy potomne ciągle pracują)</span>
*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">natychmiast powrócić ze stanem zakończenia potomka (jeśli potomek zakończył pracę i oczekuje na pobranie jego stanu zakończenia)</span>
*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">natychmiast powrócić z komunikatem awaryjnym (jeśli nie ma żadnych procesów potomnych)</span>

<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Funkcja _wait_ oczekuje na zakończenie dowolnego potomka (do tego czasu blokuje proces macierzysty). Funkcja _waitpid_ jest bardziej elastyczna, posiada możliwość określenia konkretnego PID procesu, na który ma oczekiwać, a także dodatkowe opcje (np. nieblokowanie procesu w sytuacji gdy żaden proces potomny się nie zakończył).</span> <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:#373A3C">Argument pid należy interpretować w następujący sposób:</span>

*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">pid == -1 Oczekiwanie na dowolny proces potomny. W tej sytuacji funkcja waitpid jest równoważna funkcji wait.</span>
*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">pid > 0 Oczekiwanie na proces o identyfikatorze równym pid.</span>
*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">pid == 0 Oczekiwanie na każdego potomka, którego identyfikator grupy procesów jest równy identyfikatorowi grupy procesów w procesie wywołującym tę funkcję.</span>
*   <span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">pid < -1 Oczekiwanie na każdego potomka, którego identyfikator grupy procesów jest równy wartości absolutnej argumentu pid.</span>

<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">W obydwu przypadkach statloc to wskaźnik do miejsca w pamięci, gdzie zostanie przekazany status zakończenia procesu potomnego (można go zignorować, przekazując wartość NULL).</span>

<span lang="PL" style="font-size:18.0pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Kończenie procesów</span>

<span lang="PL" style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Istnieje kilka możliwych sposobów na zakończenie procesu:</span>

*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">zakończenie normalne</span>

*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">wywołanie instrukcji</span>**<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
          color:red"> _return_ </span>**<span style="font-size:
          11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">w funkcji </span><span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">main</span>
*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">wywołanie funkcji </span>**_<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
          color:red">exit</span>_**<span style="font-size:11.5pt;font-family:
          &quot;Segoe UI&quot;,sans-serif"> - biblioteka </span><span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">stdlib</span>
*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">wywołanie funkcji </span>**_<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
          color:red">_exit</span>_**<span style="font-size:11.5pt;font-family:
          &quot;Segoe UI&quot;,sans-serif"> - biblioteka </span><span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">unistd</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C"> </span>

*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">zakończenie awaryjne</span>

*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">wywołanie funkcji </span>**_<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
          color:red">abort</span>_**<span style="font-size:11.5pt;font-family:
          &quot;Segoe UI&quot;,sans-serif"> - generuje sygnał SIGABORT</span>
*   **<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:red">odebranie sygnału</span>**

<span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Funkcje _exit_ i __exit_</span>

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">    void exit( int status )</span>**

**<span style="font-size:10.0pt;font-family:Consolas;
color:red">    void _exit( int status )</span>**

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Funkcja __exit_ natychmiast kończy działanie programu i powoduje powrót do jądra systemu. Funkcja _exit_ natomiast, dokonuje pewnych operacji porządkowych - kończy działanie procesu, który ją wykonał i powoduje przekazanie w odpowiednie miejsce tablicy procesów wartości _status_, która może zostać odebrana i zinterpretowana przez proces macierzysty. Jeśli proces macierzysty został zakończony, a istnieją procesy potomne - to wykonanie ich nie jest zakłócone, ale ich identyfikator procesu macierzystego wszystkich procesów potomnych otrzyma wartość 1 będącą identyfikatorem procesu _init_ (proces potomny staje się sierotą (ang. orphant) i jest „adoptowany" przez proces systemowy _init_). Funkcja _exit_ zdefiniowana jest w pliku </span><span style="font-size:10.0pt;font-family:Consolas;color:#E83E8C">stdlib.h</span><span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">.</span>

<span style="font-size:13.5pt;font-family:&quot;inherit&quot;,serif;color:#373A3C">Polecenie kill</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Polecenie kill przesyła sygnał do wskazanego procesu w systemie. Standardowo wywołanie programu powoduje wysyłanie sygnału nakazującego procesowi zakończenie pracy. Proces zapisuje wtedy swoje wewnętrzne dane i kończy pracę. Kill może przesyłać procesom różnego rodzaju sygnały. Są to na przykład:</span>

*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">SIGTERM – programowe zamknięcie procesu (15, domyślny sygnał)</span>
*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">SIGKILL – unicestwienie procesu, powoduje utratę wszystkich zawartych w nm danych (9)</span>
*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">SIGSTOP – zatrzymanie procesu bez utraty danych</span>
*   <span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif">SIGCONT – wznowienie zatrzymanego procesu</span>

<span style="font-size:11.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;color:#373A3C">Czasami może zdarzyć się sytuacja, iż proces nie chce się zamknąć sygnałem SIGTERM, bo jest przez coś blokowany. Wtedy definitywnie możemy go unicestwić sygnałem SIGKILL, lecz spowoduje to utratę danych wewnętrznych procesu.</span>

<span lang="PL"> </span>

</div>
