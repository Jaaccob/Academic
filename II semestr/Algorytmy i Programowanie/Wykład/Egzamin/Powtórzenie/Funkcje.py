"""
                                    Arguemnty formalne, aktualne, domyślne
#----------------------------------------------------------------------------------------------------------------------#
Wiesz już dobrze, że w definicji i deklaracji funkcji może znajdować się lista argumentów. Ta lista argumentów
nazywana jest listą argumentów formalnych natomiast argumenty znajdujące się w deklaracji funkcji nazywane są
argumentami formalnymi.

Każda funkcja może być oczywiście uruchomiona z różnymi wartościami argumentów. Takie uruchomienie funkcji nazywamy
wywołaniem funkcji, natomiast argumenty przekazane do funkcji w momencie jej wywołania nazywamy argumentami aktualnymi.

Argument domyślny – domyślna wartość argumentu – to wartość typu zgodnego z typem pewnego parametru, zdefiniowana
przez programistę w deklaracji podprogramu, która zostanie użyta jako argument (parametr aktualny), przypisany do
danego parametru (parametru formalnego)
"""
from functools import reduce

import apply as apply


def porownaj(a=1, b=1):  # <- arguemnty domyślne
    # def porownaj(a,b): #<- argumenty formalne
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


print(porownaj(2, 1))  # <- arguemnty aktualne

"""
                                    Wartości zwracane - return, yield. python
#----------------------------------------------------------------------------------------------------------------------#
Można powiedzieć, że tego słowa kluczowego używa się podobnie do return. Podczas gdy wywołamy return przekazujemy na 
stałe kontrolę do miejsca w kodzie, który wywołał funkcję (ang. caller). Yield również przekazuje kontrolę, ale tylko 
tymczasowo. Tym samym tak jakby „usypia” funkcję w której został wywołany i zapamiętuje jej stan lokalny.

Każda funkcja zawierająca instrukcję yield jest funkcją generatora, a każdy generator to iterator. Generatory w 
Pythonie to sposób na łatwiejszą implementację iteratorów. Zamiast pisania tzw. boilerplate’u (powtarzalny, 
nadmiarowy kod) typowego dla definiowania iteratorów przy użyciu klas, możemy napisać prostą i krótszą funkcję z 
instrukcją yield.
"""


def fibonacci(limit):
    iteration = 0
    a, b = 0, 1
    while iteration <= limit:
        yield a
        a, b = b, a + b
        iteration += 1


gen_expr = (x ** 2 for x in range(10))
print(next(gen_expr))


def __gen(exp):
    for x in exp:
        yield x ** 2


gen_expr = __gen(iter(range(10)))
print(next(gen_expr))

"""
                                        Zmienne lokalne i globalne.
#----------------------------------------------------------------------------------------------------------------------#
W dużym uproszczeniu różnica między tymi dwoma rodzajami zmiennych jest następująca: zmienne globalne są to takie 
zmienne, które są dostępne w całym programie i przez cały czas jego działania, natomiast zmienne lokalne są dostępne 
tylko w pewnej części programu, zazwyczaj tylko w pewnej chwili działania programu, a nie przez cały czas.
"""

"""
                            Funkcje map, filter, reduce, zip. Wyrażenia lambda.
#----------------------------------------------------------------------------------------------------------------------#
Forma lambda służy do tworzenia małych, anonimowych funkcji. Jej składnia jest następująca: lambda parametry: wyrażenie
"""
sum2 = lambda x, y: x + y
print(sum2(3, 4))

"""
Funkcja apply( ) przyjmuje jako pierwszy argument funkcję, a jako drugi krotkę zawierającą listę jej parametrów. 
"""

boki = (5, 7)
pole = lambda a, b: a * b
obwod = lambda a, b: a + b
print(apply.apply(pole, boki))
print(apply.apply(obwod, boki))

"""
Funkcja map( ) przyjmuje jako parametry funkcję oraz jedną lub więcej sekwencji. Jej działanie polega na wykonaniu 
funkcji dla każdego elementu sekwencji i zwróceniu listy otrzymanych rezultatów:
"""
mapa = map(int, [0.5, 2.3, 3.9])
print(next(mapa))
print(next(mapa))
print(next(mapa))

"""
Funkcja zip( ) służy do konsolidacji danych. Funkcja zip( ) przyjmuje jako parametry funkcję oraz jedną lub więcej 
sekwencji, po czym zwraca listę krotek, których poszczególne elementy pochodzą z poszczególnych sekwencji.
"""
print(next(zip("abcdef", [1, 2, 3, 4, 5, 6])))

"""
Funkcja filter( ) służy do filtrowania danych. Funkcja filter( ) przyjmuje jako parametry funkcję oraz sekwencję, po 
czym zwraca sekwencję zawierającą te elementy sekwencji wejściowej, dla których funkcja zwróciła wartość logiczną True
"""
samogloski = 'aeiou'
samogloska = lambda x: x.lower() in samogloski
print(samogloska('a'))
print(samogloska('A'))
print(list(filter(samogloska, "Ala ma kota, kot ma Ale")))
print(list(filter(lambda x: x % 2 - 1, range(0, 11))))

"""
Funkcja reduce( ) służy do agregowania danych. Funkcja reduce( ) przyjmuje jako parametry funkcję oraz sekwencję, 
zwraca pojedynczą wartość. Na początek wykonuje funkcję dla dwóch pierwszych elementów sekwencji, następnie wykonuje 
funkcję dla otrzymanego w pierwszym kroku rezultatu i trzeciego elementu sekwencji, następnie wykonuje funkcję dla 
otrzymanego w drugim kroku rezultatu i czwartego elementu sekwencji, itd., aż dojdzie do końca sekwencji. 
Np.: suma elementów:
"""

print(reduce(lambda x, y: x + y, [1, 2, 3]))

"""
Bardzo ogólnie i jeszcze niezbyt precyzyjnie możemy powiedzieć, że generator jest pewnego rodzaju funkcją. Funkcja ta 
może zostać wstrzymana oraz wznowiona od miejsca, w którym została wstrzymana. Na podstawie zapamiętanego, stanu 
możliwe jest zwracanie różnych wartości podczas kolejnych wstrzymań funkcji.
"""


def liczby():
    for i in range(11):
        yield i * 2


for parzysta in liczby():
    print(parzysta)
