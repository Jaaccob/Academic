import Fifo
import LinkedList

kolejka = Fifo.Kolejka_Fifo
lista = LinkedList.LinkedList
#Przeanalizuj wyniki wykooania ciągu następujących operacji
# a) za pomocą podanej na wykładzie listy cyklicznej (zakładamy, że początkowo pusta
# tablica ma 6 miejsc).

print("Kolejka")
Q = kolejka(6)
Q.enQueue(4)
Q.enQueue(1)
Q.enQueue(3)
print(Q.deQueue())
Q.enQueue(8)
print(Q.deQueue())
Q.enQueue(4)
Q.enQueue(5)
print(Q.deQueue())
Q.enQueue(2)
Q.enQueue(1)

#Wynik tych operacji to 4/1/3 czyli pierwsze elementy kolejki
# b) za pomocą listy dowiązanej (podanie takiej pełnej implementacji jest też zadaniem
# na laboratorium).

print("Lista :")
L = lista()
L.append(4)
L.append(1)
L.append(3)
print(L.pop())
L.append(8)
print(L.pop())
L.append(4)
L.append(5)
print(L.pop())
L.append(2)
L.append(1)

#Wynik tych operacji to 3/8/5 czyli ostatnie elementy na liście po ich dodaniu